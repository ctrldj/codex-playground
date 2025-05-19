## In one sentence, what this folder does
This folder contains the **folder-automation** tool. It sets up client job folders with template documents.
The module now resides under `apps/estimations/folder-automation/`.

After following the setup steps in the repository `README.md`, run it with:
```powershell
python -m folder_automation "ClientName" "JobName"
```

### Optional graphical interface

Launch the GUI instead of the command line:

```powershell
python -m folder_automation.gui
```

To package this GUI as a Windows executable (requires `pyinstaller`):

```powershell
pip install pyinstaller
python -m folder_automation.build_exe
```
The `folder_automation_gui.exe` file will appear in the `dist` folder.
Run the generated executable without Python:
```powershell
dist\folder_automation_gui.exe
```