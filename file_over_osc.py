'''
file_over_osc.py
author: Dealga McArdle, 2015

'''

import time
import sys
import os.path

import sublime
import sublime_plugin

TEMP_PATH = '/home/zeffii/Desktop/OSC/fp.io'


class FileOverOsc(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        file_name = view.file_name()
        print(file_name)

        with open(TEMP_PATH, 'w') as f:
            f.write(file_name)
