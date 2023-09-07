import schedule
import sys
from ..settings import SETTINGS

def createSchedule():
    settingsObject = SETTINGS()
    schedule.every().day.at(settingsObject.endTime).do(endProgram)

def checkEndTimer():
    schedule.run_pending() 

def endProgram():
    print("Time is up. Ending the program now!")
    sys.exit(0)