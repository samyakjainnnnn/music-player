from settings import SETTINGS 
import modules.endtimer as endtimer
import os
import vlc
import keyboard
import time


def userInteractions(mediaPlayer, settings, songNumber):
    try:      
        while mediaPlayer.get_state() != vlc.State.Ended:
            if(settings.endTimeEnabled):
                endtimer.checkEndTimer() #Due to the way this loop iterates, we check the endtimer over here
            if(settings.skipEnabled):
                if keyboard.is_pressed(settings.skipInput):
                    break

            if(settings.goBackEnabled):
                if keyboard.is_pressed(settings.goBackInput):
                    if songNumber != 0:
                        songNumber = songNumber - 2 
                    else:
                        songNumber = -1 
                    break
        return songNumber
    
    except Exception:
        print("An error has occurred in the process.")


def playMusic():
    try:
        settings = SETTINGS() 
        if(settings.endTimeEnabled):
            endtimer.createSchedule()

        directoryContent = os.listdir(settings.directory) 
        vlcInstance = vlc.Instance()
        mediaPlayer = vlcInstance.media_player_new()

        songNumber = 0 

        while True:
            musicFile = directoryContent[songNumber] 
            time.sleep(0.5) 
            musicFilePath = os.path.join(settings.directory, musicFile) 
            vlcMedia = vlcInstance.media_new(musicFilePath) 
            mediaPlayer.set_media(vlcMedia)
            mediaPlayer.play()

            if(settings.notifyPlay):
                print("Now playing " + musicFile)
            songNumber = userInteractions(mediaPlayer, settings, songNumber)      
            mediaPlayer.stop()

            songNumber = songNumber + 1 

    except Exception:
        print("An error has occurred in the process.")
