'''
file_over_osc.py
author: Dealga McArdle, 2015

'''
import argparse
import time
import sys
import os.path

import sublime
import sublime_plugin

import pythonosc
from pythonosc import osc_message_builder
from pythonosc import udp_client


class FileOverOsc(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        file_name = view.file_name()
        print(file_name)

        client = udp_client.UDPClient("127.0.0.1", 6449)

        msg = osc_message_builder.OscMessageBuilder(address="/filepath")
        msg.add_arg(file_name)
        msg = msg.build()
        client.send(msg)
