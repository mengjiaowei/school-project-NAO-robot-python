import sys
from naoqi import ALProxy

IP = "192.168.0.1"
PORT = 9559

try:
    tts = ALProxy("ALTextToSpeech", IP, PORT)
except Exception,e:
    print "Could not create proxy to ALTextToSpeech"
    print "Error was: ",e
    sys.exit(1)
    
tts.say("hello")
#this line makes robot say a test
