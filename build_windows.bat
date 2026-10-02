@echo off
setlocal
cd /d "%~dp0"

set "PYTHON_COMMAND=py -3.11"
py -3.11 --version >nul 2>nul
if errorlevel 1 (
    where python >nul 2>nul
    if errorlevel 1 goto :python_missing
    python --version | findstr /B /C:"Python 3.11." >nul
    if errorlevel 1 goto :python_missing
    set "PYTHON_COMMAND=python"
)

%PYTHON_COMMAND% -m venv .venv
if errorlevel 1 (
    echo Python 3.11 bulunamadi veya sanal ortam olusturulamadi.
    pause
    exit /b 1
)

call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
if errorlevel 1 goto :failed

python -m pip install -r requirements.txt
if errorlevel 1 goto :failed

python -m PyInstaller --noconfirm --clean --windowed --name BarisAI --collect-all kivy --collect-all kivy_deps.sdl2 --collect-all kivy_deps.glew --collect-all kivy_deps.angle main.py
if errorlevel 1 goto :failed

echo.
echo Derleme tamamlandi: dist\BarisAI\BarisAI.exe
echo EXE'yi tasirken dist\BarisAI klasorunun tamamini kopyalayin.
pause
exit /b 0

:python_missing
echo 64 bit Python 3.11 bulunamadi. Python'u kurup tekrar deneyin.
pause
exit /b 1

:failed
echo.
echo Derleme basarisiz. Yukaridaki hata mesajini kontrol edin.
pause
exit /b 1