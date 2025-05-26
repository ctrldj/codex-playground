## In one sentence, what this file does
Setup and usage guide for the Alta Estimator tool.

# Alta Estimator

A desktop tool that calculates scaffold costs. It uses PySide6 for the interface and saves estimates to PDF.

## Setup

- Install Python 3.13
- Install dependencies
  ```powershell
  pip install -r requirements.txt
  ```

## How to run

- Launch the GUI
  ```powershell
  python -m alta_estimator.app.gui
  ```

## Build the executable

- Ensure PyInstaller is installed
  ```powershell
  pip install pyinstaller
  pyinstaller alta.spec
  ```

## Glossary

- **PySide6** – Library for building Qt-based GUIs in Python.
- **PDF** – Portable Document Format used for saving the estimate.
