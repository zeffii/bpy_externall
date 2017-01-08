import sublime
import sublime_plugin
import tempfile
import os

TEMP_PATH = os.path.join(tempfile.gettempdir(), 'bpy_external.io')

# you can not symlink this file into the SublimeText folder
# sublime will not find its contents. You must copy it to
#    /home/zeffii/.config/sublime-text-3/Packages/User
# or equivalent.
#
# hotkey, suggestion.
# { "keys": ["ctrl+shift+a"], "command": "file_over_io" }


class FileOverIo(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        file_name = view.file_name()
        print(file_name)

        with open(TEMP_PATH, 'w') as f:
            f.write(file_name)
