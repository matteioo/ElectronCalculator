# -*- mode: python -*-

block_cipher = None


a = Analysis(['cli_calc.py'],
             pathex=['/home/val/Documents/git/ElectronCalculator/py'],
             binaries=[],
             datas=[],
             hiddenimports=['_frozen_input_lib_external', '_winreg', '_scproxy', 'java', 'vms_lib', 'winreg', 'org.python', 'nt', 'msvcrt', '_winapi', '_dummy_threading', 'org'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='cli_calc',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='cli_calc')
