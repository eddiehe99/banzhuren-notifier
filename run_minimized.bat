@echo off
@REM start /min cmd /k "open_the_notice.bat"
@REM chcp 65001 >nul
set "CURRENT_DIR=%~dp0"
start /min "" "%CURRENT_DIR%open_the_notice.bat"