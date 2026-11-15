@echo off
setlocal
set PHP_BIN=C:\Users\visha\AppData\Local\Microsoft\WinGet\Packages\PHP.PHP.8.3_Microsoft.Winget.Source_8wekyb3d8bbwe\php.exe
set SITE_DIR=%~dp0wordpress
set PORT=8080

echo ========================================================
echo   Starting WordPress Server at http://localhost:%PORT%
echo ========================================================
echo Press Ctrl+C in this window anytime to stop the server.
echo Opening browser...

timeout /t 2 /nobreak >nul
start http://localhost:%PORT%/

"%PHP_BIN%" -S localhost:%PORT% -t "%SITE_DIR%"
pause
