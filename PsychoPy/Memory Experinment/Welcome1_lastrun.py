#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on November 04, 2019, at 14:29
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'Welcome1'  # from the Builder filename that created this script
expInfo = {'Intials (Ex: VS)': '', 'ID Number (Ex: 001)': '001', 'Date (Ex: 01/01/2019)': '', 'Time (Ex: 2:30am)': '', 'Skill Level (Ex: Novice, Intermediate, or Expert) ': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\varun\\Desktop\\Research\\PsychoPy\\Memory Experinment\\Welcome1_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1714, 1143], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "WelcomeScreen"
WelcomeScreenClock = core.Clock()
textWelcome = visual.TextStim(win=win, name='textWelcome',
    text='Welcome to Our Experinment\n\nPlease have a seat and go over the instructions with the reseracher\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
keyWelcome = keyboard.Keyboard()

# Initialize components for Routine "blankRoutine"
blankRoutineClock = core.Clock()
textBlank = visual.TextStim(win=win, name='textBlank',
    text='\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Study_Trial"
Study_TrialClock = core.Clock()
textStudyWord = visual.TextStim(win=win, name='textStudyWord',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "blankRoutine"
blankRoutineClock = core.Clock()
textBlank = visual.TextStim(win=win, name='textBlank',
    text='\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "WaitScreen"
WaitScreenClock = core.Clock()
textWait = visual.TextStim(win=win, name='textWait',
    text='Please get the researcher',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
keyWait = keyboard.Keyboard()

# Initialize components for Routine "testTrial"
testTrialClock = core.Clock()
textWord = visual.TextStim(win=win, name='textWord',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
keyWord = keyboard.Keyboard()

# Initialize components for Routine "blankRoutine"
blankRoutineClock = core.Clock()
textBlank = visual.TextStim(win=win, name='textBlank',
    text='\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "endScreen"
endScreenClock = core.Clock()
textEnd = visual.TextStim(win=win, name='textEnd',
    text='Thanks for participating \n\nPlease see the researcher now',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "WelcomeScreen"-------
# update component parameters for each repeat
keyWelcome.keys = []
keyWelcome.rt = []
# keep track of which components have finished
WelcomeScreenComponents = [textWelcome, keyWelcome]
for thisComponent in WelcomeScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "WelcomeScreen"-------
while continueRoutine:
    # get current time
    t = WelcomeScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textWelcome* updates
    if textWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textWelcome.frameNStart = frameN  # exact frame index
        textWelcome.tStart = t  # local t and not account for scr refresh
        textWelcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textWelcome, 'tStartRefresh')  # time at next scr refresh
        textWelcome.setAutoDraw(True)
    
    # *keyWelcome* updates
    waitOnFlip = False
    if keyWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyWelcome.frameNStart = frameN  # exact frame index
        keyWelcome.tStart = t  # local t and not account for scr refresh
        keyWelcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyWelcome, 'tStartRefresh')  # time at next scr refresh
        keyWelcome.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyWelcome.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyWelcome.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyWelcome.status == STARTED and not waitOnFlip:
        theseKeys = keyWelcome.getKeys(keyList=['space', 'enter'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            keyWelcome.keys = theseKeys.name  # just the last key pressed
            keyWelcome.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WelcomeScreen"-------
for thisComponent in WelcomeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textWelcome.started', textWelcome.tStartRefresh)
thisExp.addData('textWelcome.stopped', textWelcome.tStopRefresh)
# check responses
if keyWelcome.keys in ['', [], None]:  # No response was made
    keyWelcome.keys = None
thisExp.addData('keyWelcome.keys',keyWelcome.keys)
if keyWelcome.keys != None:  # we had a response
    thisExp.addData('keyWelcome.rt', keyWelcome.rt)
thisExp.addData('keyWelcome.started', keyWelcome.tStartRefresh)
thisExp.addData('keyWelcome.stopped', keyWelcome.tStopRefresh)
thisExp.nextEntry()
# the Routine "WelcomeScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "blankRoutine"-------
routineTimer.add(0.500000)
# update component parameters for each repeat
# keep track of which components have finished
blankRoutineComponents = [textBlank]
for thisComponent in blankRoutineComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
blankRoutineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "blankRoutine"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = blankRoutineClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=blankRoutineClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textBlank* updates
    if textBlank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textBlank.frameNStart = frameN  # exact frame index
        textBlank.tStart = t  # local t and not account for scr refresh
        textBlank.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textBlank, 'tStartRefresh')  # time at next scr refresh
        textBlank.setAutoDraw(True)
    if textBlank.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textBlank.tStartRefresh + 0.5-frameTolerance:
            # keep track of stop time/frame for later
            textBlank.tStop = t  # not accounting for scr refresh
            textBlank.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textBlank, 'tStopRefresh')  # time at next scr refresh
            textBlank.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blankRoutineComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "blankRoutine"-------
for thisComponent in blankRoutineComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textBlank.started', textBlank.tStartRefresh)
thisExp.addData('textBlank.stopped', textBlank.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trialsStudy = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('wordstimuli.xlsx', selection='0:6'),
    seed=None, name='trialsStudy')
thisExp.addLoop(trialsStudy)  # add the loop to the experiment
thisTrialsStudy = trialsStudy.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialsStudy.rgb)
if thisTrialsStudy != None:
    for paramName in thisTrialsStudy:
        exec('{} = thisTrialsStudy[paramName]'.format(paramName))

for thisTrialsStudy in trialsStudy:
    currentLoop = trialsStudy
    # abbreviate parameter names if possible (e.g. rgb = thisTrialsStudy.rgb)
    if thisTrialsStudy != None:
        for paramName in thisTrialsStudy:
            exec('{} = thisTrialsStudy[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Study_Trial"-------
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    textStudyWord.setColor(WordColor, colorSpace='rgb')
    textStudyWord.setText(WordItem
)
    # keep track of which components have finished
    Study_TrialComponents = [textStudyWord]
    for thisComponent in Study_TrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Study_TrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Study_Trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Study_TrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Study_TrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textStudyWord* updates
        if textStudyWord.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            textStudyWord.frameNStart = frameN  # exact frame index
            textStudyWord.tStart = t  # local t and not account for scr refresh
            textStudyWord.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textStudyWord, 'tStartRefresh')  # time at next scr refresh
            textStudyWord.setAutoDraw(True)
        if textStudyWord.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textStudyWord.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                textStudyWord.tStop = t  # not accounting for scr refresh
                textStudyWord.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textStudyWord, 'tStopRefresh')  # time at next scr refresh
                textStudyWord.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Study_TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Study_Trial"-------
    for thisComponent in Study_TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialsStudy.addData('textStudyWord.started', textStudyWord.tStartRefresh)
    trialsStudy.addData('textStudyWord.stopped', textStudyWord.tStopRefresh)
    
    # ------Prepare to start Routine "blankRoutine"-------
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blankRoutineComponents = [textBlank]
    for thisComponent in blankRoutineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blankRoutineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "blankRoutine"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blankRoutineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blankRoutineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textBlank* updates
        if textBlank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textBlank.frameNStart = frameN  # exact frame index
            textBlank.tStart = t  # local t and not account for scr refresh
            textBlank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textBlank, 'tStartRefresh')  # time at next scr refresh
            textBlank.setAutoDraw(True)
        if textBlank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textBlank.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                textBlank.tStop = t  # not accounting for scr refresh
                textBlank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textBlank, 'tStopRefresh')  # time at next scr refresh
                textBlank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankRoutineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blankRoutine"-------
    for thisComponent in blankRoutineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialsStudy.addData('textBlank.started', textBlank.tStartRefresh)
    trialsStudy.addData('textBlank.stopped', textBlank.tStopRefresh)
# completed 1 repeats of 'trialsStudy'


# ------Prepare to start Routine "WaitScreen"-------
# update component parameters for each repeat
keyWait.keys = []
keyWait.rt = []
# keep track of which components have finished
WaitScreenComponents = [textWait, keyWait]
for thisComponent in WaitScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WaitScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "WaitScreen"-------
while continueRoutine:
    # get current time
    t = WaitScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WaitScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textWait* updates
    if textWait.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textWait.frameNStart = frameN  # exact frame index
        textWait.tStart = t  # local t and not account for scr refresh
        textWait.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textWait, 'tStartRefresh')  # time at next scr refresh
        textWait.setAutoDraw(True)
    
    # *keyWait* updates
    waitOnFlip = False
    if keyWait.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        keyWait.frameNStart = frameN  # exact frame index
        keyWait.tStart = t  # local t and not account for scr refresh
        keyWait.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyWait, 'tStartRefresh')  # time at next scr refresh
        keyWait.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyWait.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyWait.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyWait.status == STARTED and not waitOnFlip:
        theseKeys = keyWait.getKeys(keyList=['v'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            keyWait.keys = theseKeys.name  # just the last key pressed
            keyWait.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WaitScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WaitScreen"-------
for thisComponent in WaitScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textWait.started', textWait.tStartRefresh)
thisExp.addData('textWait.stopped', textWait.tStopRefresh)
# check responses
if keyWait.keys in ['', [], None]:  # No response was made
    keyWait.keys = None
thisExp.addData('keyWait.keys',keyWait.keys)
if keyWait.keys != None:  # we had a response
    thisExp.addData('keyWait.rt', keyWait.rt)
thisExp.addData('keyWait.started', keyWait.tStartRefresh)
thisExp.addData('keyWait.stopped', keyWait.tStopRefresh)
thisExp.nextEntry()
# the Routine "WaitScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('wordstimuli.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "testTrial"-------
    # update component parameters for each repeat
    textWord.setText(WordItem)
    keyWord.keys = []
    keyWord.rt = []
    # keep track of which components have finished
    testTrialComponents = [textWord, keyWord]
    for thisComponent in testTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    testTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "testTrial"-------
    while continueRoutine:
        # get current time
        t = testTrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=testTrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textWord* updates
        if textWord.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textWord.frameNStart = frameN  # exact frame index
            textWord.tStart = t  # local t and not account for scr refresh
            textWord.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textWord, 'tStartRefresh')  # time at next scr refresh
            textWord.setAutoDraw(True)
        
        # *keyWord* updates
        waitOnFlip = False
        if keyWord.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyWord.frameNStart = frameN  # exact frame index
            keyWord.tStart = t  # local t and not account for scr refresh
            keyWord.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyWord, 'tStartRefresh')  # time at next scr refresh
            keyWord.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyWord.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyWord.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyWord.status == STARTED and not waitOnFlip:
            theseKeys = keyWord.getKeys(keyList=['y', 'n'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                keyWord.keys = theseKeys.name  # just the last key pressed
                keyWord.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "testTrial"-------
    for thisComponent in testTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('textWord.started', textWord.tStartRefresh)
    trials.addData('textWord.stopped', textWord.tStopRefresh)
    # check responses
    if keyWord.keys in ['', [], None]:  # No response was made
        keyWord.keys = None
    trials.addData('keyWord.keys',keyWord.keys)
    if keyWord.keys != None:  # we had a response
        trials.addData('keyWord.rt', keyWord.rt)
    trials.addData('keyWord.started', keyWord.tStartRefresh)
    trials.addData('keyWord.stopped', keyWord.tStopRefresh)
    # the Routine "testTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blankRoutine"-------
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blankRoutineComponents = [textBlank]
    for thisComponent in blankRoutineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blankRoutineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "blankRoutine"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blankRoutineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blankRoutineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textBlank* updates
        if textBlank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textBlank.frameNStart = frameN  # exact frame index
            textBlank.tStart = t  # local t and not account for scr refresh
            textBlank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textBlank, 'tStartRefresh')  # time at next scr refresh
            textBlank.setAutoDraw(True)
        if textBlank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textBlank.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                textBlank.tStop = t  # not accounting for scr refresh
                textBlank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textBlank, 'tStopRefresh')  # time at next scr refresh
                textBlank.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankRoutineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blankRoutine"-------
    for thisComponent in blankRoutineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('textBlank.started', textBlank.tStartRefresh)
    trials.addData('textBlank.stopped', textBlank.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "endScreen"-------
routineTimer.add(20.000000)
# update component parameters for each repeat
# keep track of which components have finished
endScreenComponents = [textEnd]
for thisComponent in endScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "endScreen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textEnd* updates
    if textEnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textEnd.frameNStart = frameN  # exact frame index
        textEnd.tStart = t  # local t and not account for scr refresh
        textEnd.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textEnd, 'tStartRefresh')  # time at next scr refresh
        textEnd.setAutoDraw(True)
    if textEnd.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > textEnd.tStartRefresh + 20-frameTolerance:
            # keep track of stop time/frame for later
            textEnd.tStop = t  # not accounting for scr refresh
            textEnd.frameNStop = frameN  # exact frame index
            win.timeOnFlip(textEnd, 'tStopRefresh')  # time at next scr refresh
            textEnd.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "endScreen"-------
for thisComponent in endScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textEnd.started', textEnd.tStartRefresh)
thisExp.addData('textEnd.stopped', textEnd.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
