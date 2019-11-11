
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# There is little experiment if the participant cannot give any input.
# Here we changed assignment 2 a bit so that it waits for a keys, rather
# than waiting 5 s. Note that we need to import the event module from
# PsychoPy to make this work.
from psychopy import core, visual, event

win = visual.Window([400,340], monitor = 'textMonitor')
textString = "What is your favortie color? \n"
message = visual.TextStim(win,text = textString)


message.draw()
win.flip()
c = event.waitKeys()
string = ' '.join([str(elem) for elem in c])
message = visual.TextStim(win, text = textString + string)
message.draw()
win.flip()
core.wait(3)

win.close()
core.quit()