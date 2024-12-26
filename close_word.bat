@echo off

echo Trying to close Word process automatically
echo.

chcp 65001 >nul

:: check whether the WPS process exists
wmic process where "name='WINWORD.EXE'" get processid | findstr /r /c:"[0-9]" >nul 2>&1

if %errorlevel% equ 0 (
    echo Word process is running.

    :: Try to kill the Word process
    taskkill /F /IM "WINWORD.EXE"

    :: Kill the  WPS process
    @REM taskkill /F /IM "wps.exe"
) else (
    echo Word process is not running.
)