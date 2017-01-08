#!/bin/bash

# B3D_DIR=$HOME/src/blender-git/build-master/bin
tmpfile=$(mktemp -t bpy_externall.XXXXXX).py

{
	echo 'import bpy'
	echo 'import addon_utils'
	echo 'addon_utils.enable("bpy_externall")'
	echo 'bpy.ops.wm.bpy_externall_server(speed=1, mode="start")'
} >$tmpfile

blender -P $tmpfile
rm $tmpfile
