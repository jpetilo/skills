"""Confere apenas exemplos sintéticos de contrato; não executa app nem valida visual."""
import copy
import json
import math
import unittest
from pathlib import Path

CASES = {case["id"]: case for case in json.loads(
    (Path(__file__).resolve().parents[1] / "references" / "simulacoes.fixture.json")
    .read_text(encoding="utf-8"))["casos"]}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_links(case):
    ids = []
    for records in case["entidades"].values():
        ids.extend(record["id"] for record in records)
    require(len(ids) == len(set(ids)), "ID duplicado")
    groups = case["entidades"]
    lookup = {record["id"]: record for records in groups.values() for record in records}
    relations = {"empresa_id": "empresa", "objetivo_id": "objetivo",
                 "alinhado_id": "objetivo", "livro_id": "livro"}
    for records in groups.values():
        for record in records:
            for field, owner in relations.items():
                value = record.get(field)
                if value is not None:
                    require(value in {r["id"] for r in groups.get(owner, [])}, "referência órfã")
            if record.get("alinhado_id"):
                require(lookup[record["alinhado_id"]]["empresa_id"] == record["empresa_id"],
                        "alinhamento fora da empresa")
    operations = {op["id"]: op for op in case["operacoes"]}
    require(case["acao"]["operacao"] in operations, "operação sem dono")
    operation = operations[case["acao"]["operacao"]]
    if operation["situacao"] == "proposta":
        require(case["acao"]["modalidade"] != "real existente", "proposta apresentada como real")
        require(operation["verificacao"] != "executada", "execução inventada")


def contribution(kr, current=None):
    current = kr["atual"] if current is None else current
    require(kr["meta"] > kr["inicial"], "meta inválida")
    require(math.isfinite(current) and current >= kr["inicial"], "medição inválida")
    return min(100.0, 100.0 * (current - kr["inicial"]) / (kr["meta"] - kr["inicial"]))


def progress(case, objective, override=None):
    values = [contribution(kr, (override or {}).get(kr["id"], kr["atual"]))
              for kr in case["entidades"]["kr"] if kr["objetivo_id"] == objective]
    return sum(values) / len(values) if values else None


def available(case):
    book = case["entidades"]["livro"][0]
    return book["exemplares"] - sum(
        loan["quantidade"] for loan in case["entidades"]["emprestimo"]
        if loan["livro_id"] == book["id"])


def reserve(balance, amount):
    require(type(amount) is int and 1 <= amount <= balance, "reserva inválida")
    return balance - amount


class ContractExamples(unittest.TestCase):
    def test_two_domains_have_consistent_references(self):
        for case in CASES.values():
            check_links(case)

    def test_okr_expected_values_and_no_rollup(self):
        case = CASES["okr"]
        self.assertEqual(progress(case, "OBJ-T"), case["esperados"]["antes"])
        self.assertEqual(progress(case, "OBJ-T", {"KR-A": 60}), case["esperados"]["apos_confirmar_60"])
        self.assertEqual(progress(case, "OBJ-E", {"KR-A": 60}), case["esperados"]["empresarial"])
        self.assertEqual(contribution(case["entidades"]["kr"][1], 120), case["esperados"]["limite_120"])

    def test_okr_cancel_and_invalid_preserve_confirmed_input(self):
        action = copy.deepcopy(CASES["okr"]["acao"])
        action["rascunho"] = 60
        self.assertEqual(action["confirmado"], CASES["okr"]["esperados"]["cancelar"])
        with self.assertRaises(ValueError):
            contribution(CASES["okr"]["entidades"]["kr"][1], 19)
        self.assertEqual(action["confirmado"], 40)

    def test_invalid_target_is_rejected(self):
        kr = copy.deepcopy(CASES["okr"]["entidades"]["kr"][1])
        kr["meta"] = kr["inicial"]
        with self.assertRaises(ValueError):
            contribution(kr)

    def test_library_balance_confirm_cancel(self):
        case = CASES["biblioteca"]
        balance = available(case)
        self.assertEqual(balance, case["esperados"]["disponiveis"])
        self.assertEqual(reserve(balance, 1), case["esperados"]["apos_reservar_1"])
        self.assertEqual(available(case), case["esperados"]["cancelar"])

    def test_library_excess_and_fraction_rejected_without_changing_fixture(self):
        case = copy.deepcopy(CASES["biblioteca"])
        before = copy.deepcopy(case)
        for amount in (2, 0, 0.5, True):
            with self.assertRaises(ValueError):
                reserve(available(case), amount)
        self.assertEqual(case, before)

    def test_orphan_fixture_is_rejected(self):
        case = copy.deepcopy(CASES["biblioteca"])
        case["entidades"]["emprestimo"][0]["livro_id"] = "AUSENTE"
        with self.assertRaises(ValueError):
            check_links(case)

    def test_duplicate_id_is_rejected(self):
        case = copy.deepcopy(CASES["okr"])
        case["entidades"]["kr"].append(copy.deepcopy(case["entidades"]["kr"][0]))
        with self.assertRaises(ValueError):
            check_links(case)

    def test_missing_operation_is_rejected(self):
        case = copy.deepcopy(CASES["biblioteca"])
        case["acao"]["operacao"] = "AUSENTE"
        with self.assertRaises(ValueError):
            check_links(case)

    def test_simulation_cannot_claim_real_execution(self):
        case = copy.deepcopy(CASES["biblioteca"])
        case["acao"]["modalidade"] = "real existente"
        with self.assertRaises(ValueError):
            check_links(case)
        case = copy.deepcopy(CASES["biblioteca"])
        case["operacoes"][0]["verificacao"] = "executada"
        with self.assertRaises(ValueError):
            check_links(case)


if __name__ == "__main__":
    unittest.main(verbosity=2)
