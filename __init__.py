# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "bpy externall",
    "author": "Dealga McArdle",
    "version": (0, 1),
    "blender": (2, 7, 6),
    "location": "",
    "description": "",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Text Editor"
}


import argparse
import importlib
import threading

import bpy
from bpy.props import (
    BoolProperty, StringProperty, FloatProperty
)

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


NOT_FOUND = 0
FOUND = 1
STOPPED = 2
RUNNING = 3


try:
    STATUS = FOUND
    if ('pythonosc' in locals()):
        print('bp_externall : reload event. handled')
    else:
        # from pythonosc import osc_message_builder
        # from pythonosc import udp_client
        import pythonosc
        from pythonosc import osc_server
        from pythonosc import dispatcher
        print('bp_externall loaded pythonosc')

except:
    STATUS = NOT_FOUND
    print('python osc not found!, or failed to reimport')


osc_statemachine = {'status': STATUS}
osc_statemachine['filepath'] = ""
osc_statemachine['tempfile'] = '/home/zeffii/Desktop/OSC/fp.io'


def filepath_handler(uh, fp):
    temp_path = osc_statemachine['tempfile']
    with open('/home/zeffii/Desktop/OSC/fp.io', 'w') as f:
        print('received: ', fp)
        f.write(fp)


def filepath_read_handler():
    temp_path = osc_statemachine['tempfile']

    fp = ""
    with open(temp_path) as f:
        fp = f.read()

    # make empty file
    with open(temp_path, 'w') as f:
        pass

    return fp


def start_server_comms():
    ip = "127.0.0.1"
    port = 6449

    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default=ip, help="The ip to listen on")
    parser.add_argument("--port", type=int, default=port, help="The port to listen on")
    args = parser.parse_args()

    disp = dispatcher.Dispatcher()
    disp.map("/filepath", filepath_handler)
    osc_statemachine['dispatcher'] = disp
    osc_statemachine['args'] = args

    server = osc_server.ForkingOSCUDPServer((args.ip, args.port), disp)
    server_thread = threading.Thread(target=server.serve_forever)
    osc_statemachine['server'] = server
    server_thread.start()

    print("Serving on {}".format(server.server_address))


class BPYExternallOscClient(bpy.types.Operator, object):

    bl_idname = "wm.bpy_externall_osc_server"
    bl_label = "start and stop osc server"

    _timer = None
    speed = FloatProperty()
    mode = StringProperty()

    def process(self):
        fp = filepath_read_handler()
        print('process: ', fp)
        stripped_fp = fp.strip()
        if stripped_fp:
            print('action', stripped_fp)

    def modal(self, context, event):

        if osc_statemachine['status'] == STOPPED:
            osc_statemachine['server'].shutdown()
            self.cancel(context)
            return {'FINISHED'}

        if not (event.type == 'TIMER'):
            return {'PASS_THROUGH'}

        self.process()
        return {'PASS_THROUGH'}

    def event_dispatcher(self, context, type_op):
        if type_op == 'start':

            wm = context.window_manager
            self._timer = wm.event_timer_add(self.speed, context.window)
            wm.modal_handler_add(self)

            osc_statemachine['status'] = RUNNING
            start_server_comms()

        if type_op == 'end':
            osc_statemachine['status'] = STOPPED

    def execute(self, context):
        self.event_dispatcher(context, self.mode)
        return {'RUNNING_MODAL'}

    def cancel(self, context):
        wm = context.window_manager
        wm.event_timer_remove(self._timer)


class BPYExternallOSCpanel(bpy.types.Panel):

    bl_idname = "BPYExternallOSCpanel"
    bl_label = "bpy externall OSC panel"
    bl_space_type = 'TEXT_EDITOR'
    bl_region_type = 'UI'
    # bl_options = {'DEFAULT_CLOSED'}
    use_pin = True

    def draw(self, context):
        layout = self.layout
        col = layout.column()

        state = osc_statemachine['status']

        # exit early
        if state == NOT_FOUND:
            col.label('failed to (re)import pythonosc - see console')
            return

        # promising! continue
        tstr = ''
        if state in {FOUND, STOPPED}:
            tstr = 'start'
        elif state == RUNNING:
            col.label('listening on /filepath')
            tstr = 'end'

        if tstr:
            op = col.operator('wm.bpy_externall_osc_server', text=tstr)
            op.mode = tstr
            op.speed = 1


def register():
    bpy.utils.register_class(BPYExternallOSCpanel)
    bpy.utils.register_class(BPYExternallOscClient)


def unregister():
    bpy.utils.unregister_class(BPYExternallOSCpanel)
    bpy.utils.unregister_class(BPYExternallOscClient)
