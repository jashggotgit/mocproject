$ppt = New-Object -ComObject PowerPoint.Application
$filePath = "C:\Users\Jashith Masand\Desktop\CN\ALVEARE_Research_Paper_Presentation.pptx"
$pdfPath = "C:\Users\Jashith Masand\Desktop\CN\ALVEARE_Research_Paper_Presentation.pdf"
$slidesDir = "C:\Users\Jashith Masand\Desktop\CN\slides_img"

if (!(Test-Path $slidesDir)) {
    New-Item -ItemType Directory -Path $slidesDir | Out-Null
}

$pres = $ppt.Presentations.Open($filePath, [Microsoft.Office.Core.MsoTriState]::msoTrue, [Microsoft.Office.Core.MsoTriState]::msoFalse, [Microsoft.Office.Core.MsoTriState]::msoFalse)
$pres.SaveAs($pdfPath, 32) # 32 = ppSaveAsPDF

$i = 1
foreach ($slide in $pres.Slides) {
    $slideImg = Join-Path $slidesDir ("slide_{0:D2}.png" -f $i)
    $slide.Export($slideImg, "PNG", 1920, 1080)
    $i++
}

$pres.Close()
$ppt.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($ppt) | Out-Null
Write-Host "Export completed successfully!"
