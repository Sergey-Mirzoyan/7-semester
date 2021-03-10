from cx_Freeze import setup, Executable

executables = [Executable('main.py',
targetName='Main.exe',)]


includes = ['pygame', 'pygame_menu', 'os']

zip_include_packages = [ 'pygame', 'pygame_menu', 'os' ]

include_files = [
'простые числа.py',
'installer.py',
'certificate.key']

options = {
'build_exe': {
'include_msvcr': True,
'includes': includes,
'zip_include_packages': zip_include_packages,
'build_exe': 'build_windows',
'include_files': include_files,
}
}

setup(name=' main',
version='0.0.3',
description='My app',
executables=executables,
options=options)
