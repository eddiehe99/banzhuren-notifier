@echo off
@REM start /min cmd /k "open-the-notice.bat"
@REM chcp 65001 >nul
set "current_dir=%~dp0"
start /min "" "%current_dir%open-the-notice.bat"