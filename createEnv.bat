@echo off
REM Change directory to the location of your project

REM Check if Python is installed
python --version
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed or not added to PATH.
    exit /b 1
)

python -m venv sam_venv
echo Virtual environment created.

call sam_venv\Scripts\activate

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

@echo off
pip install -r requirements.txt

cd sam2
pip install -e .
pip install -e ".[notebooks]"


echo Virtual environment setup complete.
pause