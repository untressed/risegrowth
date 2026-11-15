@echo off
set PHP_BIN=C:\Users\visha\AppData\Local\Microsoft\WinGet\Packages\PHP.PHP.8.3_Microsoft.Winget.Source_8wekyb3d8bbwe\php.exe
set WP_CLI=%~dp0wp-cli.phar
"%PHP_BIN%" "%WP_CLI%" --path="%~dp0wordpress" %*
