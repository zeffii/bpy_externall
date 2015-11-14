# bpy_externall
execute scripts in a running Blender session from any decent text editor.

dependencies:  requires the python-osc module, but this can be done much simpler without it (I see now after coding it the hard way)

```python

"""
## INSTALLATION 

  python-osc:

  - https://pypi.python.org/pypi/python-osc#downloads
  - Blender: drop the zip/tar into Blender's modules folder
  - System python (3.4):  `python3.4 -m pip install python-osc`

  'bpy_externall' add-on:

  - In UserPreferences "install from file", and navigate to 
    the zip that contains this file.
  - Save preferences and or Ctrl+U to store the addon's enabled
    state in the default.blend

## RECEIVER

When enabled and active this panel will use pythonosc
and a modal operator to regularly poll an OSC path.
Something like: address="/filepath"

The OSC path will be queued with a full python filepath
that Blender must execute. After execution the modal
operator continues to poll and do nothing until a new
filepath is queued.

## SENDER

The exact implementation will be up to the user. This
repository will provide a small plugin for Sublime
Text to demonstrate the OSC sending.

see `osc_sending.py` for an example of how to send a filepath 
to the temp.

"""

```
