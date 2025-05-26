# ## In one sentence, what this file does
# PyInstaller spec file to build the Alta Estimator executable.

block_cipher = None

a = Analysis(
    ['-m', 'alta_estimator.app.gui'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='AltaEstimator',
    debug=False,
    strip=False,
    upx=True,
    console=True,
)
