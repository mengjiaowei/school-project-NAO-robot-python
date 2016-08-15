# Filename: takeGun.py

from naoqi import ALProxy
from proxy import makeProxy
import time

myProxy = makeProxy()

class recieving():

    def gun(self):
        
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([ 3.00000])
        keys.append([ -0.16418])

        names.append("HeadYaw")
        times.append([ 3.00000])
        keys.append([ -0.01078])

        names.append("LAnklePitch")
        times.append([ 3.00000])
        keys.append([ 0.07973])

        names.append("LAnkleRoll")
        times.append([ 3.00000])
        keys.append([ -0.11654])

        names.append("LElbowRoll")
        times.append([ 3.00000])
        keys.append([ -0.37732])

        names.append("LElbowYaw")
        times.append([ 3.00000])
        keys.append([ -1.18736])

        names.append("LHand")
        times.append([ 3.00000])
        keys.append([ 0.00538])
        
        names.append("LHipPitch")
        times.append([ 3.00000])
        keys.append([ 0.13503])
            
        names.append("LHipRoll")
        times.append([ 3.00000])
        keys.append([ 0.11509])
        
        names.append("LHipYawPitch")
        times.append([ 3.00000])
        keys.append([ -0.17330])
        
        names.append("LKneePitch")
        times.append([ 3.00000])
        keys.append([ -0.09055])
        
        names.append("LShoulderPitch")
        times.append([ 3.00000])
        keys.append([ 1.48027])
        
        names.append("LShoulderRoll")
        times.append([ 3.00000])
        keys.append([ 0.07359])
        
        names.append("LWristYaw")
        times.append([ 3.00000])
        keys.append([ 0.08740])
        
        names.append("RAnklePitch")
        times.append([ 3.00000])
        keys.append([ 0.10282])
        
        names.append("RAnkleRoll")
        times.append([ 3.00000])
        keys.append([ 0.07367])

        names.append("RElbowRoll")
        times.append([ 3.00000])
        keys.append([ 0.89772])

        names.append("RElbowYaw")
        times.append([ 3.00000])
        keys.append([ 0.75162])

        names.append("RHand")
        times.append([0.5, 6.0])
        keys.append([1.0, 0.46])

        names.append("RHipPitch")
        times.append([ 3.00000])
        keys.append([ 0.13188])

        names.append("RHipRoll")
        times.append([ 3.00000])
        keys.append([ -0.06439])

        names.append("RHipYawPitch")
        times.append([ 3.00000])
        keys.append([ -0.17330])

        names.append("RKneePitch")
        times.append([ 3.00000])
        keys.append([ -0.08893])

        names.append("RShoulderPitch")
        times.append([ 1.00000])
        keys.append([1.0])

        names.append("RShoulderRoll")
        times.append([ 3.00000])
        keys.append([ 0.31416])

        names.append("RWristYaw")
        times.append([ 3.00000])
        keys.append([ 0.37119])


        try:        
            myProxy.setAngleInterpolation(names, keys, times)
        except BaseException, err:
          print err
