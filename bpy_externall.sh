#!/bin/bash

# Fill in with your own path to blender's binary
# B3D_DIR=$HOME/src/blender-git/build-master/bin
tmpfile=$(mktemp -t bpy_externall.XXXXXX).py

{
	echo 'import bpy'
	echo 'import addon_utils'
	echo 'addon_utils.enable("bpy_externall")'
	echo 'bpy.ops.wm.bpy_externall_server(speed=1, mode="start")'
} >$tmpfile

# Path and binary calling temp python file above
# $B3D_DIR/blender -P $tmpfile
blender -P $tmpfile
# Remove temp file after blender exits
rm $tmpfile
