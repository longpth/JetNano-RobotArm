import logging
from websocket_server import WebsocketServer
import Util

class MyServer(object):

  def new_client(self, client, server):
    Util.DebugInfo('New client connect {}'.format(client))

  def message_received(self, client, server, message):
    Util.DebugInfo('Client {} send {}'.format(client['address'], message))
    self.process_servos(message)

  def process_servos(self, message):
    data = message.split(',')
    if data[0] == 'servo' and len(data)==5:
      print('rotate all')
      data = [int(i) for i in data[1:5]]
      self.servo_control.rotateAll(data)

  def __init__(self, port, servo_control):
    self.server = WebsocketServer(host='127.0.0.1', port=port, loglevel=logging.INFO)
    self.server.set_fn_new_client(self.new_client)
    self.servo_control = servo_control
    self.server.set_fn_message_received(self.message_received)

  def start(self):
    self.server.run_forever()
