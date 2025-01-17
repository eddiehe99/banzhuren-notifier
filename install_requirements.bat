@echo off
REM 获取当前脚本所在的目录
setlocal
set "scriptDirectory=%~dp0"

REM 设置 requirements.txt 文件的路径
set "requirementsFilePath=%scriptDirectory%requirements.txt"

REM 检查 requirements.txt 文件是否存在
if not exist "%requirementsFilePath%" (
    echo Error: requirements.txt not found in %scriptDirectory%
    pause
    exit /b 1
)

REM 检查是否安装了 Python
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in the system PATH.
    pause
    exit /b 1
)

REM 切换到南方科技大学（SUSTech）的 PyPI 镜像源
echo Switching to SUSTech PyPI mirror...
python -m pip config set global.index-url https://mirrors.sustech.edu.cn/pypi/simple

REM 升级 pip
echo Upgrading pip...
python -m pip install --upgrade pip

REM 安装 requirements.txt 中的依赖包
echo Installing Python dependencies from %requirementsFilePath%...
python -m pip install -r "%requirementsFilePath%"

REM 检查 pip 安装是否成功
if %errorlevel% equ 0 (
    echo Dependencies installed successfully.
) else (
    echo Error: Failed to install dependencies.
    pause
    exit /b 1
)

endlocal
@REM pause