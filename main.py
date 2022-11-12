import MyServer
import ServoControl
import subprocess
import signal

def main():
  servo = ServoControl.ServoControl(4)
  server = MyServer.MyServer(1080, servo)
  cmds = 'node-red'
  p = subprocess.Popen(cmds, start_new_session=True)
  server.start() #run forever
  p.send_signal(signal.SIGINT)
  print('main exit')

if __name__ == '__main__':
  main()