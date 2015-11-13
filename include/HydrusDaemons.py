import HydrusConstants as HC
import HydrusExceptions
import os
import sys
import threading
import time
import traceback
import HydrusData

def DAEMONMaintainDB( controller ):
    
    if controller.CurrentlyIdle():
        
        controller.MaintainDB()
        
    
def DAEMONMaintainMemory( controller ):
    
    controller.MaintainMemory()
    
def DAEMONSleepCheck( controller ):
    
    controller.SleepCheck()
    