# -*- mode: python ; coding: utf-8 -*-

import sys
sys.setrecursionlimit(5000)

block_cipher = None

added_files = [
    ('C:\\dev\\repo\\frypan\\Frypan_Controllers','Frypan_Controllers'),
    ('C:\\dev\\repo\\frypan\\Frypan_Window','Frypan_Window'),
    ('C:\\dev\\repo\\frypan\\LICENSE','.'),
    ('C:\\dev\\repo\\frypan\\INFO','.'),
]

a = Analysis(['Frypan.py'],
             pathex=['C:\\dev\\repo\\frypan'],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[
                 'certifi',
                 'IPython',
                 'jedi',
                 'jsonschema',
                 'lib2to3',
                 'lxml',
                 'markupsafe',
                 'nbconvert',
                 'nbformat',
                 'notebook',
                 'numexpr',
                 'PIL',
                 'scipy',
                 'share',
                 'tornado',
                 'zmq'
             ],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Frypan',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Frypan')
