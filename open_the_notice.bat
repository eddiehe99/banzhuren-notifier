:: Using Chinese may cause unexpected errors!!!

:: This bat operates with the Task Scheduler on Windows.
:: It is used to open the daily notice schedully.

@echo off
setlocal ENABLEEXTENSIONS ENABLEDELAYEDEXPANSION
@REM setlocal ENABLEEXTENSIONS

echo Trying to open today's notification automatically
echo.

@REM for /f %%a in ('date /t') do (
@REM     @REM echo %%a
@REM     set date=%%a
@REM     set year=!date:~0,4!
@REM     set month=!date:~5,2!
@REM     set day=!date:~8,2!
@REM     set formattedDate=!year!-!month!-!day!
@REM )

@REM echo date: !date!


for /f "tokens=2 delims==. " %%a in ('wmic os get localdatetime /value') do (
    set "DATETIME=%%a"
    echo datetime: !DATETIME!
    set "YEAR=!DATETIME:~0,4!"
    set "MONTH=!DATETIME:~4,2!"
    set "DAY=!DATETIME:~6,2!"
    set "FORMATTED_DATE=!YEAR!-!MONTH!-!DAY!"
    echo Formatted Date: !FORMATTED_DATE!
)

echo.


:: Select UTF-8 encoding
:: Necessary. Otherwise, the Chinese hostname may cause encoding errors.
:: UTF-8 encoding selection could not be set before formattedDate.
:: As the `date /t` may return date in Chinese format.
chcp 65001 >nul

set "CURRENT_DIR=%~dp0"
for /f "tokens=1,2 delims==" %%i in (%CURRENT_DIR%configuration.txt) do (
    set "%%i=%%j"
    @REM echo %%i is %%j
)

set "HOSTNAME=%HOSTNAME%"
set "SHARED_FOLDER=%SHARED_FOLDER%"
set "SHARED_DIR=\\%HOSTNAME%\%SHARED_FOLDER%"
set "USERNAME=%USERNAME%"
set "PASSWORD=%PASSWORD%"
set "NOTICE_FILENAME=%FORMATTED_DATE% 通知.docx"

:: ping the hostname
ping %HOSTNAME% -n 1 >nul 2>&1

if %errorlevel% equ 0 (
    echo successfully ping %HOSTNAME%
    echo Trying to open %SHARED_DIR%\%NOTICE_FILENAME%

    :: Try to connect to the sharedPath
    echo connecting to %SHARED_DIR%
    net use %SHARED_DIR% /user:%USERNAME% %PASSWORD% >nul 2>&1

    :: Check the connection status
    if %errorlevel% equ 0 (
        echo SHARED_DIR accessible: %SHARED_DIR%

        :: check whether the notice file exists
        dir "%SHARED_DIR%\%NOTICE_FILENAME%" >nul 2>&1

        if errorlevel 1 (
            echo the notice file does not exist: %SHARED_DIR%\%NOTICE_FILENAME%
        ) else (
            echo the notice file exists: %SHARED_DIR%\%NOTICE_FILENAME%

            :: Try to open the notice file
            start "" "%SHARED_DIR%\%NOTICE_FILENAME%"
        )

        :: Disconnect
        net use %SHARED_DIR% /delete >nul 2>&1
    ) else (
        echo SHARED_DIR unaccessible: %SHARED_DIR%
    )
) else (
    echo ping %HOSTNAME% time out
)

endlocal

exit