# bpy_externall
execute scripts in a running Blender session from any decent text editor.

dependencies:  requires the OSC module.

```python

"""
## INSTALLATION python osc:

- https://pypi.python.org/pypi/python-osc#downloads
- drop the zip/tar into Blender's modules folder

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

"""

```
