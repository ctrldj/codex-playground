## In one sentence, what this file does
# Basic environment setup commands for Windows.

Write-Output "Creating virtual environment..."
python -m venv .venv
Write-Output "Activating virtual environment..."
.venv\Scripts\Activate.ps1
Write-Output "Installing dependencies..."
pip install -e ..\..
