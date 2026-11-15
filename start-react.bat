@echo off
set NODE_BIN=C:\Users\visha\.gemini\antigravity-ide\scratch\wordpress-site\tools\node
set PATH=%NODE_BIN%;%PATH%

echo ================================================================
echo   RISE GROWTH GROUP - Headless WordPress + React Architecture
echo ================================================================
echo.
echo   Backend (WordPress CMS)  : http://localhost:8080/
echo   Frontend (React SPA)     : http://localhost:3000/
echo   WordPress Admin          : http://localhost:8080/wp-admin
echo   REST API                 : http://localhost:8080/?rest_route=/wp/v2/pages
echo.
echo Starting React frontend at http://localhost:3000/ ...
echo Press Ctrl+C to stop the React server.
echo.

timeout /t 2 /nobreak >nul
start http://localhost:3000/

cd /d "%~dp0frontend-react"
npm run dev
pause
