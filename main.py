import os
import hugchat
import subprocess

import eel

from engine.features import *
from engine.command import *
from engine.auth import recoganize



def start():
    eel.init("www")
    
    playAssistantSound()
    @eel.expose
    def init():
        subprocess.call([r'device.bat'])
        eel.hideLoader()
        speak(" Ready for Face Authentication.")
        flag = recoganize.AuthenticateFace()
        if flag == 1:
            eel.hideFaceAuth()
            speak("Authentication successful.")
            eel.hideFaceAuthSuccess()
            speak(" welcome to AI, How can I assist you today?")
            eel.hideStart()
            playAssistantSound()
        else:
            speak("Authentication failed. Please try again.")
            return

    #init()  # <-- Add this line to call init() automatically

    os.system('start msedge.exe --app="http://localhost:8000/index.html"')
    eel.start('index.html', mode=None, host='localhost', block=True)