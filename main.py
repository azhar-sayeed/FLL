#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks import DriveBase

# Write your program here
brick.sound.beep()

MotorB = Motor (Port.B)
MotorC = Motor (Port.C)

Cookie = DriveBase (MotorB, MotorC, 56, 60)
Cookie.drive(200, 0)
Cookie.drive_distance(100, 0, 300)

def 