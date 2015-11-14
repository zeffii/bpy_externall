import argparse
import random
import time

from pythonosc import osc_message_builder
from pythonosc import udp_client

IP = "ip of OSC server"
PORT = "port OSC server listens on"

paths = [
  'path one',
  'path two',
  'path three']


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1", help=IP)
    parser.add_argument("--port", type=int, default=6449, help=PORT)
    args = parser.parse_args()

    client = udp_client.UDPClient(args.ip, args.port)


    msg = osc_message_builder.OscMessageBuilder(address="/filepath")
    msg.add_arg(random.choice(paths))
    msg = msg.build()
    client.send(msg)

