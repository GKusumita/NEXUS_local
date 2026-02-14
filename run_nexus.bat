@echo off
echo ==========================================
echo      NEXUS Local Environment Setup
echo ==========================================

REM Check if venv exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
) else (
    echo Virtual environment already exists.
)

REM Activate venv
echo Activating virtual environment...
call venv\Scripts\activate

REM Install dependencies
if exist "requirements.txt" (
    echo Installing dependencies...
    pip install -r requirements.txt
)

echo.
echo ==========================================
echo      Starting NEXUS Application
echo ==========================================
python main.py

pause
