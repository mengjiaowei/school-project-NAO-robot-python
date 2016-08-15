import sys
import math
from naoqi import ALProxy

names = list()
times = list()
keys = list()


def sayHello(self):
    impo = self.aup.loadFile("/home/nao/baoqi/Of_course_I_39_m_a_Terminator")
    self.aup.play(impo)

IP = "192.168.0.1"
PORT = 9559

try:
    proxy = ALProxy("ALMotion", IP, PORT)
except Exception,e:
    print "Could not create proxy to ALMotion"
    print "Error was: ",e
    sys.exit(1)
    

proxy.stiffnessInterpolation("Body", 1.0, 0.1) 
proxy.walkInit()

# Example showing the walkTo command 
# The units for this command are meters and radians 
names.append("RHand")
times.append([0.5])
keys.append([0.6])
proxy.angleInterpolation(names, keys, times, True)

x=0.375
y =0.0
theta=0.0
proxy.walkTo(x, y, theta)

self.sayHello()

x=0.0
y=0.0
theta = -3.14
proxy.walkTo(x, y, theta)

x=0.375
y =0.0
theta=0.0
proxy.walkTo(x, y, theta)
# Will block until walk Task is finished

########
# NOTE #
########
# If walkTo() method does nothing on the robot,
# please refer to special walk protection in the
# setWalkTargetVelocity() method description below.
