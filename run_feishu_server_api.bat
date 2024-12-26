@echo off
setlocal
set "currentDir=%~dp0"

set "pythonFilePath=%currentDir%feishu_server_api.py"

python "%pythonFilePath%"
endlocal

@REM pause