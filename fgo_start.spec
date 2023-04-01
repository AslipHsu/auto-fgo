# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['fgo_start.py', 'check_card.py', 'fgo_click.py', 'fgo_controller.py', 'fgo_ui.py', 'screenshot.py', 'set_attack.py', 'set_skill.py', 'set_support_class.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='fgo_start',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\User\\Desktop\\build-fgo-2\\gd.ico'],
)
