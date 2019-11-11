
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from psychopy import core, visual
from showText import showText
 
# Create a window
win = visual.Window([400,300], monitor="testMonitor")
 
# Create a stimulus for a certain window

myText = "nr:   grade: \n"

grades = [7.1,4.5,6.3,5.8,8.2]
for studentNumber, grade in enumerate(grades):
    myText += str(studentNumber) + " ,    " + str(grade) + "\n"
    
message = visual.TextStim(win, text = myText)
showText(win,message)

