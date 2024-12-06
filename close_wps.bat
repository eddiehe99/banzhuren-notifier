@echo off

echo Trying to close WPS process automatically
echo.

chcp 65001 >nul

:: check whether the WPS process exists
wmic process where "name='wps.exe'" get processid | findstr /r /c:"[0-9]" >nul 2>&1

if %errorlevel% equ 0 (
    echo WPS process is running.

    :: Try to kill the Word process
    @REM taskkill /F /IM "WINWORD.EXE"

    :: Kill the  WPS process
    taskkill /F /IM "wps.exe"
) else (
    echo WPS process is not running.
)