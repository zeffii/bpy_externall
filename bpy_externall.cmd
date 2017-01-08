@echo off

set B3D_DIR="C:\Program Files\Blender Foundation\Blender"
set SERVERSTART=%TEMP%\bpy_externall.py

echo import bpy; import addon_utils; addon_utils.enable('bpy_externall'); bpy.ops.wm.bpy_externall_server(speed=1, mode='start') > %SERVERSTART%

%B3D_DIR%\blender.exe -P %SERVERSTART%
del /Q %SERVERSTART%
