
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# My functions.
  
from psychopy import core, visual, event
import math, time


def debugLog(text):
    tSinceMidnight = time.time() % 86400
    tSinceWholeHour= tSinceMidnight % 3600
    minutes = tSinceWholeHour / 60
    hours = tSinceMidnight / 3600
    seconds = tSinceMidnight % 60
    
    print("log {:02d}:{:02d}:{:f}: {}".format(int(hours), int(minutes), seconds, text))