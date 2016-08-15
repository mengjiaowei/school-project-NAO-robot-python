# Filename: proxy.py

from naoqi import ALProxy
import time
# Creates an ip and port to be used within the class
ip = "192.168.0.1"
port = 9559


class makeProxy():
    # Initializes the proxies whenever an object of this class i created
    landmarkProxy = ALProxy("ALLandMarkDetection", ip, port)
    memoryProxy = ALProxy("ALMemory", ip, port)
    motionProxy = ALProxy("ALMotion", ip, port)
    aup = ALProxy("ALAudioPlayer", ip, port)
        
    # Returns the data of the landmark detected
    def getMemoryData(self, landmark):
        return self.memoryProxy.getData(landmark)

    # Retrieves current transform from ALMotion to be used to calculate the
    # robots position to the naomark
    def getMotionTransform(self, currentCamera):
        return self.motionProxy.getTransform(currentCamera, 2, True)

    # Used to set the position all the robots joints using 3 different lists
    def setAngleInterpolation(self, names, keys, times):
        return self.motionProxy.angleInterpolation(names, keys, times, True)

    # Unstiffs the robots joints so it can move
    def unstiffRobot(self):
        return self.motionProxy.stiffnessInterpolation("Body", 1.0, 0.1)

    # Initialize the robot into a position so it can start walking
    def initiateWalk(self):
        return self.motionProxy.walkInit()

    # Tells the robot where to walk accordingly
    def robotWalkTo(self, x, y, theta):
        return self.motionProxy.moveTo(x, y, theta)

    # Makes the robot to stop moving, in case something went wrong
    def stopWalk(self):
        return self.motionProxy.stopMove()

    # Plays the set file
    def sayTerminator(self):
        fileTwo = self.aup.loadFile("/home/nao/naoqi/Of_course_I_39_m_a_Terminator.wav")
        #time.sleep(1)
        self.aup.play(fileTwo)

    # Plays the set file
    def sayHasta(self):
        fileId = self.aup.loadFile("/home/nao/naoqi/Terminator_2_-_Hasta_La_Vista_Baby.wav")
        #time.sleep(1)
        self.aup.play(fileId)
    
    # Subscribes to landmarkproxy
    def subscribeToLandmark(self):
        self.landmarkProxy.subscribe("landmarkTest")

    # Unsubsubscribes to landmarkproxy
    def unsubscribeToLandmark(self):
        self.landmarkProxy.unsubscribe("landmarkTest")

