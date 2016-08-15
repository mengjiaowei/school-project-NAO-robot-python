# Filename: detectLandmarks.py

from naoqi import ALProxy
from proxy import makeProxy
import math
import almath

# Set here the size of the landmark in meters.
landmarkTheoreticalSize = 0.195 

# Set here the current camera ("CameraTop" or "CameraBottom").
currentCamera = "CameraTop"

# Create makeProxy object
myProxy = makeProxy()


class calculateData():

    # Different objects to be used within the class
    robotToLandmark = 0
    markData = list()
    distanceFromCameraToLandmark = 0
    wyCamera = 0
    wzCamera = 0
    
    # Detect a naomark
    def detectMark(self):

        # Subcribe to landmark
        myProxy.subscribeToLandmark()
        
        # Loops until a landmark is detected
        self.markData = myProxy.getMemoryData("LandmarkDetected")
        while (len(self.markData) == 0):
            self.markData = myProxy.getMemoryData("LandmarkDetected")

        # Unsubscribe to landmark
        myProxy.unsubscribeToLandmark()

    # Retrives and sets different kinds of data to be used later    
    def calcData(self):

        # Retrieve landmark center position in radians.
        self.wzCamera = self.markData[1][0][0][1]
        self.wyCamera = self.markData[1][0][0][2]

        # Retrieve landmark angular size in radians.
        angularSize = self.markData[1][0][0][3]

        # Compute distance to landmark.
        self.distanceFromCameraToLandmark = landmarkTheoreticalSize / ( 2 * math.tan( angularSize / 2))

    # Calculates the different data from the class above, to get the exact
    # position of the robot and distance to the naomark
    def computeData(self):
        
        # Get current camera position in NAO space.
        transform = myProxy.getMotionTransform(currentCamera)
        transformList = almath.vectorFloat(transform)
        robotToCamera = almath.Transform(transformList)

        # Compute the rotation to point towards the landmark.
        cameraToLandmarkRotationTransform = almath.Transform_from3DRotation(0, self.wyCamera, self.wzCamera)

        # Compute the translation to reach the landmark.
        cameraToLandmarkTranslationTransform = almath.Transform(self.distanceFromCameraToLandmark, 0, 0)

        # Combine all transformations to get the landmark position in NAO space.
        self.robotToLandmark = robotToCamera * cameraToLandmarkRotationTransform *cameraToLandmarkTranslationTransform
        
    # Returns the distance to the naomark in meters
    def getResults(self):
        print "x " + str(self.robotToLandmark.r1_c4) + " (in meters)"
        print "y " + str(self.robotToLandmark.r2_c4) + " (in meters)"
        print "z " + str(self.robotToLandmark.r3_c4) + " (in meters)"

    # make the robot walk and place himself one meter in front of the naomark
    def robotWalk(self):

        # Get the parameters
        distX = self.robotToLandmark.r1_c4
        y = self.robotToLandmark.r2_c4
        theta = 0.0 #self.robotToLandmark.r3_c4

        x = distX - 1

        # Unstiff the robot
        myProxy.unstiffRobot()

        # Call initiateWalk()
        myProxy.initiateWalk()

        # Make the robot walk
        myProxy.robotWalkTo(x, y, theta)

    def back(self):
        
        # Get the parameters
        x = 0.375
        y = 0.375
        theta = 0.0
        myProxy.unstiffRobot()
        myProxy.initiateWalk()
        # Walk forward
        myProxy.robotWalkTo(x, y, theta) 

        
        
    def andForth(self):
        
        x = 0.375
        y = 0.375
        theta = 0.0
        myProxy.unstiffRobot()
        myProxy.initiateWalk()
        # Walk forward
        myProxy.robotWalkTo(x, y, theta)

        # Get the parameters
        x = 0.0
        y = 0.0
        theta = -3.14
        myProxy.unstiffRobot()
        myProxy.initiateWalk()
        # Walk forward
        myProxy.robotWalkTo(x, y, theta)

    # Makes the robot raise his arm and pull the trigger of the nerfgun
    def shoot(self):

        # The height of the naomark 
        ZuluValue = self.robotToLandmark.r3_c4
        b = 1.0

        # Currently doesn't work
        # Raise the robots arm dependning on the height of the naomark
        if ZuluValue <= 0.20 and ZuluValue > 0.25:
            b = 1.4
        elif ZuluValue <= 0.25 and ZuluValue > 0.30:
            b = 1.3
        elif ZuluValue <= 0.30 and ZuluValue > 0.35:
            b = 1.2
        elif ZuluValue <= 0.35 and ZuluValue > 0.40:
            b = 1.1
        elif ZuluValue <= 0.40 and ZuluValue > 0.50:
            b = 1.0
        elif ZuluValue <= 0.50 and ZuluValue > 0.60:
            b = 0.9
        elif ZuluValue <= 0.60 and ZuluValue > 0.70:
            b = 0.8
        elif ZuluValue <= 0.70 and ZuluValue > 0.80:
            b = 0.7
        elif ZuluValue <= 0.80 and ZuluValue > 0.90:
            b = 0.6
        elif ZuluValue <= 0.90 and ZuluValue > 1.00:
            b = 0.5
        elif ZuluValue <= 1.00 and ZuluValue > 1.08:
            b = 0.4
        elif ZuluValue <= 1.08 and ZuluValue > 1.18:
            b = 0.35
        elif ZuluValue <= 1.18 and ZuluValue > 1.25:
            b = 0.3

        print b
        
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
        times.append([1, 4, 6, 8])
        keys.append([0.46, 0.46, 0.5, 0])

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
        keys.append([b])

        names.append("RShoulderRoll")
        times.append([ 3.00000])
        keys.append([ 0.31416])

        names.append("RWristYaw")
        times.append([ 3.00000])
        keys.append([ 0.37119])

        # Puts all the joints in position accordingly to the lists above
        # in a timeline
        try:
            myProxy.setAngleInterpolation(names, keys, times)
        except BaseException, err:
            print err
    
