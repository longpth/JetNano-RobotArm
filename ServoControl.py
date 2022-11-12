from adafruit_servokit import ServoKit
import board
import busio
import time
from approxeng.input.selectbinder import ControllerResource
import sys
# sys.setrecursionlimit(10000)

class ServoControl(object):
  def __init__(self, servo_cnt):
    # On the Jetson Nano
    # Bus 0 (pins 28,27) is board SCL_1, SDA_1 in the jetson board definition file
    # Bus 1 (pins 5, 3) is board SCL, SDA in the jetson definition file
    # Default is to Bus 1; We are using Bus 0, so we need to construct the busio first ...
    print("Initializing Servos")
    self.i2c_bus0=(busio.I2C(board.SCL, board.SDA))
    print("Initializing ServoKit")
    self.kit = ServoKit(channels=16, i2c=self.i2c_bus0)
    self.servo_cnt = servo_cnt
    degree_inits = []
    # for servo_index in range(servo_cnt):
    #   degree_inits.append(45)
    # self.rotateAll(degree_inits)
    # kit[0] is the bottom servo
    # kit[1] is the top servo
    print("Done initializing")

  def rotate(self, motor_idx, degree):
    self.kit.servo[motor_idx].angle=degree

  def rotateAll(self, degrees):
    if len(degrees) != self.servo_cnt:
      print('Number of degrees is not matched with Number of servo {}!={}'.format(len(degrees),self.servo_cnt))
    else:
      for i in range(len(degrees)):
        self.kit.servo[i].angle=degrees[i]


