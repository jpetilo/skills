param([Parameter(Mandatory=$true)][string]$Scene,[Parameter(Mandatory=$true)][string]$Output)
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Drawing
$data = Get-Content -Raw -Encoding UTF8 -LiteralPath $Scene | ConvertFrom-Json
$bitmap = [System.Drawing.Bitmap]::new([int]$data.width,[int]$data.height)
$graphics = [System.Drawing.Graphics]::FromImage($bitmap)
$graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$graphics.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit
$graphics.Clear([System.Drawing.Color]::White)
try {
    foreach($item in $data.items) {
        if($item.type -eq 'rect') {
            $brush = [System.Drawing.SolidBrush]::new([System.Drawing.ColorTranslator]::FromHtml($item.fill))
            $pen = [System.Drawing.Pen]::new([System.Drawing.ColorTranslator]::FromHtml($item.stroke),2)
            try {
                $graphics.FillRectangle($brush,[single]$item.x,[single]$item.y,[single]$item.w,[single]$item.h)
                $graphics.DrawRectangle($pen,[single]$item.x,[single]$item.y,[single]$item.w,[single]$item.h)
            } finally { $brush.Dispose(); $pen.Dispose() }
        } elseif($item.type -eq 'line') {
            $pen = [System.Drawing.Pen]::new([System.Drawing.ColorTranslator]::FromHtml($item.color),[single]$item.width)
            try {
                $points = [System.Drawing.PointF[]]@($item.points | ForEach-Object { [System.Drawing.PointF]::new([single]$_[0],[single]$_[1]) })
                $graphics.DrawLines($pen,$points)
            } finally { $pen.Dispose() }
        } elseif($item.type -eq 'text') {
            $style = if($item.bold) { [System.Drawing.FontStyle]::Bold } else { [System.Drawing.FontStyle]::Regular }
            $font = [System.Drawing.Font]::new('Segoe UI',[single]$item.size,$style,[System.Drawing.GraphicsUnit]::Pixel)
            $brush = [System.Drawing.SolidBrush]::new([System.Drawing.ColorTranslator]::FromHtml($item.color))
            try {
                $size = $graphics.MeasureString([string]$item.text,$font)
                $x = [single]$item.x
                if($item.align -eq 'center') { $x -= $size.Width / 2 }
                $y = [single]$item.y
                if($x -lt 0 -or $y -lt 0 -or ($x+$size.Width) -gt $data.width -or ($y+$size.Height) -gt $data.height) { throw ('Texto fora da imagem: ' + $item.text) }
                if($item.background) { $graphics.FillRectangle([System.Drawing.Brushes]::White,$x-4,$y,[single]($size.Width+8),[single]$size.Height) }
                $graphics.DrawString([string]$item.text,$font,$brush,$x,$y)
            } finally { $font.Dispose(); $brush.Dispose() }
        } else { throw ('Primitiva desconhecida: '+$item.type) }
    }
    $bitmap.Save($Output,[System.Drawing.Imaging.ImageFormat]::Png)
    Write-Output ('PNG renderizado localmente: '+$Output)
} finally { $graphics.Dispose(); $bitmap.Dispose() }
