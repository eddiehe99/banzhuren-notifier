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
    set datetime=%%a
    echo datetime: !datetime!
    set year=!datetime:~0,4!
    set month=!datetime:~4,2!
    set day=!datetime:~6,2!
    set formattedDate=!year!-!month!-!day!
)

echo formattedDate: !formattedDate!
echo.


:: Select UTF-8 encoding
:: Necessary. Otherwise, the Chinese hostname may cause encoding errors.
:: UTF-8 encoding selection could not be set before formattedDate.
:: As the `date /t` may return date in Chinese format.
chcp 65001 >nul

for /f "tokens=1,2 delims=:" %%i in (configuration.txt) do (
    set "%%i=%%j"
    @REM echo %%i is %%j
)

set "hostname=%hostname%"
set "sharedFolder=%sharedFolder%"
set "sharedPath=\\%hostname%\%sharedFolder%"
set "username=%username%"
set "password=%password%"
set "noticeFileName=%formattedDate% 通知.docx"

:: ping the hostname
ping %hostname% -n 1 >nul 2>&1

if %errorlevel% equ 0 (
    echo successfully ping %hostname%
    echo Trying to open %sharedPath%\%noticeFileName%

    :: Try to connect to the sharedPath
    echo connecting to %sharedPath%
    net use %sharedPath% /user:%username% %password% >nul 2>&1

    :: Check the connection status
    if %errorlevel% equ 0 (
        echo sharedPath accessible: %sharedPath%

        :: check whether the notice file exists
        dir "%sharedPath%\%noticeFileName%" >nul 2>&1

        if errorlevel 1 (
            echo the notice file does not exist: %sharedPath%\%noticeFileName%
        ) else (
            echo the notice file exists: %sharedPath%\%noticeFileName%

            :: Try to open the notice file
            start "" "%sharedPath%\%noticeFileName%"
        )

        :: Disconnect
        net use %sharedPath% /delete >nul 2>&1
    ) else (
        echo sharedPath unaccessible: %sharedPath%
    )
) else (
    echo ping %hostname% time out
)

endlocal

exit