# bpy_externall
execute scripts in a running Blender session from any decent text editor.

```python

"""
## INSTALLATION 

  'bpy_externall' add-on:

  - In UserPreferences "install from file", and navigate to 
    the zip that contains this file.
  - Save preferences and or Ctrl+U to store the addon's enabled
    state in the default.blend

## RECEIVER

When enabled and active this panel will use simple file reading to
see if a file is empty or not. If the file isn't empty then it is
assumed that its contents is infact a filename: a filepath to a .py 
file to be executed.

If the file contains a filename, it will exec the found path, and
then empty the file for the next loop. When the file contains
nothing, the modal operator will skip any execution.

## SENDER

The exact implementation will be up to the user. This
repository will provide a small plugin for Sublime
Text to demonstrate how you might send a filepath 
to the temp file.

"""

```
