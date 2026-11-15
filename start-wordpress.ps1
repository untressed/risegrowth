$phpBin = "C:\Users\visha\AppData\Local\Microsoft\WinGet\Packages\PHP.PHP.8.3_Microsoft.Winget.Source_8wekyb3d8bbwe\php.exe"
$siteDir = Join-Path $PSScriptRoot "wordpress"
$port = 8080

Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "  Starting WordPress Server at http://localhost:$port" -ForegroundColor Green
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "Opening your browser in 2 seconds..." -ForegroundColor Yellow

Start-Sleep -Seconds 2
Start-Process "http://localhost:$port/"
& $phpBin -S "localhost:$port" -t $siteDir
