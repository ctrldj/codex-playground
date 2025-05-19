## In one sentence, what this folder does
This folder contains the **folder-automation** tool. It sets up client job folders with template documents.
The module now resides under `apps/estimations/folder-automation/`.

After following the setup steps in the repository `README.md`, run it with:
```powershell
python -m folder_automation "ClientName" "JobName"
```

For a point-and-click interface run:
```powershell
python -m folder_automation.gui
```

To build a Windows executable (requires PyInstaller):
```powershell
python -m folder_automation.build_exe
```
