/***************** 
 * Welcome1 Test *
 *****************/

import { PsychoJS } from 'https://pavlovia.org/lib/core-3.2.js';
import * as core from 'https://pavlovia.org/lib/core-3.2.js';
import { TrialHandler } from 'https://pavlovia.org/lib/data-3.2.js';
import { Scheduler } from 'https://pavlovia.org/lib/util-3.2.js';
import * as util from 'https://pavlovia.org/lib/util-3.2.js';
import * as visual from 'https://pavlovia.org/lib/visual-3.2.js';
import { Sound } from 'https://pavlovia.org/lib/sound-3.2.js';

// init psychoJS:
var psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'Welcome1';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(WelcomeScreenRoutineBegin);
flowScheduler.add(WelcomeScreenRoutineEachFrame);
flowScheduler.add(WelcomeScreenRoutineEnd);
flowScheduler.add(blankRoutineRoutineBegin);
flowScheduler.add(blankRoutineRoutineEachFrame);
flowScheduler.add(blankRoutineRoutineEnd);
const trialsStudyLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsStudyLoopBegin, trialsStudyLoopScheduler);
flowScheduler.add(trialsStudyLoopScheduler);
flowScheduler.add(trialsStudyLoopEnd);
flowScheduler.add(WaitScreenRoutineBegin);
flowScheduler.add(WaitScreenRoutineEachFrame);
flowScheduler.add(WaitScreenRoutineEnd);
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin, trialsLoopScheduler);
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(endScreenRoutineBegin);
flowScheduler.add(endScreenRoutineEachFrame);
flowScheduler.add(endScreenRoutineEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({expName, expInfo});

var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '3.2.4';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0/Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0/60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}

var WelcomeScreenClock;
var textWelcome;
var keyWelcome;
var blankRoutineClock;
var textBlank;
var Study_TrialClock;
var textStudyWord;
var WaitScreenClock;
var textWait;
var keyWait;
var testTrialClock;
var textWord;
var keyWord;
var endScreenClock;
var textEnd;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "WelcomeScreen"
  WelcomeScreenClock = new util.Clock();
  textWelcome = new visual.TextStim({
    win: psychoJS.window,
    name: 'textWelcome',
    text: 'Welcome to Our Experinment\n\nPlease have a seat and go over the instructions with the reseracher\n',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  keyWelcome = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "blankRoutine"
  blankRoutineClock = new util.Clock();
  textBlank = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank',
    text: '\n',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Study_Trial"
  Study_TrialClock = new util.Clock();
  textStudyWord = new visual.TextStim({
    win: psychoJS.window,
    name: 'textStudyWord',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "blankRoutine"
  blankRoutineClock = new util.Clock();
  textBlank = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank',
    text: '\n',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "WaitScreen"
  WaitScreenClock = new util.Clock();
  textWait = new visual.TextStim({
    win: psychoJS.window,
    name: 'textWait',
    text: 'Please get the researcher',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  keyWait = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "testTrial"
  testTrialClock = new util.Clock();
  textWord = new visual.TextStim({
    win: psychoJS.window,
    name: 'textWord',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  keyWord = new core.Keyboard({psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "blankRoutine"
  blankRoutineClock = new util.Clock();
  textBlank = new visual.TextStim({
    win: psychoJS.window,
    name: 'textBlank',
    text: '\n',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "endScreen"
  endScreenClock = new util.Clock();
  textEnd = new visual.TextStim({
    win: psychoJS.window,
    name: 'textEnd',
    text: 'Thanks for participating \n\nPlease see the researcher now',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

var t;
var frameN;
var WelcomeScreenComponents;
function WelcomeScreenRoutineBegin() {
  //------Prepare to start Routine 'WelcomeScreen'-------
  t = 0;
  WelcomeScreenClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  keyWelcome.keys = undefined;
  keyWelcome.rt = undefined;
  // keep track of which components have finished
  WelcomeScreenComponents = [];
  WelcomeScreenComponents.push(textWelcome);
  WelcomeScreenComponents.push(keyWelcome);
  
  for (const thisComponent of WelcomeScreenComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var continueRoutine;
function WelcomeScreenRoutineEachFrame() {
  //------Loop for each frame of Routine 'WelcomeScreen'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = WelcomeScreenClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *textWelcome* updates
  if (t >= 0.0 && textWelcome.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    textWelcome.tStart = t;  // (not accounting for frame time here)
    textWelcome.frameNStart = frameN;  // exact frame index
    textWelcome.setAutoDraw(true);
  }

  
  // *keyWelcome* updates
  if (t >= 0.0 && keyWelcome.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    keyWelcome.tStart = t;  // (not accounting for frame time here)
    keyWelcome.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { keyWelcome.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { keyWelcome.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { keyWelcome.clearEvents(); });
  }

  if (keyWelcome.status === PsychoJS.Status.STARTED) {
    let theseKeys = keyWelcome.getKeys({keyList: ['space', 'enter'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      keyWelcome.keys = theseKeys[0].name;  // just the last key pressed
      keyWelcome.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of WelcomeScreenComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function WelcomeScreenRoutineEnd() {
  //------Ending Routine 'WelcomeScreen'-------
  for (const thisComponent of WelcomeScreenComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  psychoJS.experiment.addData('keyWelcome.keys', keyWelcome.keys);
  if (typeof keyWelcome.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('keyWelcome.rt', keyWelcome.rt);
      routineTimer.reset();
      }
  
  keyWelcome.stop();
  // the Routine "WelcomeScreen" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var blankRoutineComponents;
function blankRoutineRoutineBegin() {
  //------Prepare to start Routine 'blankRoutine'-------
  t = 0;
  blankRoutineClock.reset(); // clock
  frameN = -1;
  routineTimer.add(0.500000);
  // update component parameters for each repeat
  // keep track of which components have finished
  blankRoutineComponents = [];
  blankRoutineComponents.push(textBlank);
  
  for (const thisComponent of blankRoutineComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var frameRemains;
function blankRoutineRoutineEachFrame() {
  //------Loop for each frame of Routine 'blankRoutine'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = blankRoutineClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *textBlank* updates
  if (t >= 0.0 && textBlank.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    textBlank.tStart = t;  // (not accounting for frame time here)
    textBlank.frameNStart = frameN;  // exact frame index
    textBlank.setAutoDraw(true);
  }

  frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (textBlank.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    textBlank.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of blankRoutineComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function blankRoutineRoutineEnd() {
  //------Ending Routine 'blankRoutine'-------
  for (const thisComponent of blankRoutineComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  return Scheduler.Event.NEXT;
}

var trialsStudy;
var currentLoop;
function trialsStudyLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trialsStudy = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'wordstimuli.xlsx', '0:6'),
    seed: undefined, name: 'trialsStudy'});
  psychoJS.experiment.addLoop(trialsStudy); // add the loop to the experiment
  currentLoop = trialsStudy;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrialsStudy of trialsStudy) {
    thisScheduler.add(importConditions(trialsStudy));
    thisScheduler.add(Study_TrialRoutineBegin);
    thisScheduler.add(Study_TrialRoutineEachFrame);
    thisScheduler.add(Study_TrialRoutineEnd);
    thisScheduler.add(blankRoutineRoutineBegin);
    thisScheduler.add(blankRoutineRoutineEachFrame);
    thisScheduler.add(blankRoutineRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : false}));
  }

  return Scheduler.Event.NEXT;
}


function trialsStudyLoopEnd() {
  psychoJS.experiment.removeLoop(trialsStudy);

  return Scheduler.Event.NEXT;
}

var trials;
function trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'wordstimuli.xlsx',
    seed: undefined, name: 'trials'});
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrial of trials) {
    thisScheduler.add(importConditions(trials));
    thisScheduler.add(testTrialRoutineBegin);
    thisScheduler.add(testTrialRoutineEachFrame);
    thisScheduler.add(testTrialRoutineEnd);
    thisScheduler.add(blankRoutineRoutineBegin);
    thisScheduler.add(blankRoutineRoutineEachFrame);
    thisScheduler.add(blankRoutineRoutineEnd);
    thisScheduler.add(endLoopIteration({thisScheduler, isTrials : true}));
  }

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}

var Study_TrialComponents;
function Study_TrialRoutineBegin() {
  //------Prepare to start Routine 'Study_Trial'-------
  t = 0;
  Study_TrialClock.reset(); // clock
  frameN = -1;
  routineTimer.add(2.000000);
  // update component parameters for each repeat
  textStudyWord.setColor(new util.Color(WordColor));
  textStudyWord.setText(WordItem);
  // keep track of which components have finished
  Study_TrialComponents = [];
  Study_TrialComponents.push(textStudyWord);
  
  for (const thisComponent of Study_TrialComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function Study_TrialRoutineEachFrame() {
  //------Loop for each frame of Routine 'Study_Trial'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = Study_TrialClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *textStudyWord* updates
  if (t >= 0 && textStudyWord.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    textStudyWord.tStart = t;  // (not accounting for frame time here)
    textStudyWord.frameNStart = frameN;  // exact frame index
    textStudyWord.setAutoDraw(true);
  }

  frameRemains = 0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (textStudyWord.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    textStudyWord.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of Study_TrialComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function Study_TrialRoutineEnd() {
  //------Ending Routine 'Study_Trial'-------
  for (const thisComponent of Study_TrialComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  return Scheduler.Event.NEXT;
}

var WaitScreenComponents;
function WaitScreenRoutineBegin() {
  //------Prepare to start Routine 'WaitScreen'-------
  t = 0;
  WaitScreenClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  keyWait.keys = undefined;
  keyWait.rt = undefined;
  // keep track of which components have finished
  WaitScreenComponents = [];
  WaitScreenComponents.push(textWait);
  WaitScreenComponents.push(keyWait);
  
  for (const thisComponent of WaitScreenComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function WaitScreenRoutineEachFrame() {
  //------Loop for each frame of Routine 'WaitScreen'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = WaitScreenClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *textWait* updates
  if (t >= 0.0 && textWait.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    textWait.tStart = t;  // (not accounting for frame time here)
    textWait.frameNStart = frameN;  // exact frame index
    textWait.setAutoDraw(true);
  }

  
  // *keyWait* updates
  if (t >= 0.0 && keyWait.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    keyWait.tStart = t;  // (not accounting for frame time here)
    keyWait.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { keyWait.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { keyWait.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { keyWait.clearEvents(); });
  }

  if (keyWait.status === PsychoJS.Status.STARTED) {
    let theseKeys = keyWait.getKeys({keyList: ['v'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      keyWait.keys = theseKeys[0].name;  // just the last key pressed
      keyWait.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of WaitScreenComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function WaitScreenRoutineEnd() {
  //------Ending Routine 'WaitScreen'-------
  for (const thisComponent of WaitScreenComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  psychoJS.experiment.addData('keyWait.keys', keyWait.keys);
  if (typeof keyWait.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('keyWait.rt', keyWait.rt);
      routineTimer.reset();
      }
  
  keyWait.stop();
  // the Routine "WaitScreen" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var testTrialComponents;
function testTrialRoutineBegin() {
  //------Prepare to start Routine 'testTrial'-------
  t = 0;
  testTrialClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  textWord.setText(WordItem);
  keyWord.keys = undefined;
  keyWord.rt = undefined;
  // keep track of which components have finished
  testTrialComponents = [];
  testTrialComponents.push(textWord);
  testTrialComponents.push(keyWord);
  
  for (const thisComponent of testTrialComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function testTrialRoutineEachFrame() {
  //------Loop for each frame of Routine 'testTrial'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = testTrialClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *textWord* updates
  if (t >= 0.0 && textWord.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    textWord.tStart = t;  // (not accounting for frame time here)
    textWord.frameNStart = frameN;  // exact frame index
    textWord.setAutoDraw(true);
  }

  
  // *keyWord* updates
  if (t >= 0.0 && keyWord.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    keyWord.tStart = t;  // (not accounting for frame time here)
    keyWord.frameNStart = frameN;  // exact frame index
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { keyWord.clock.reset(); });  // t=0 on next screen flip
    psychoJS.window.callOnFlip(function() { keyWord.start(); }); // start on screen flip
    psychoJS.window.callOnFlip(function() { keyWord.clearEvents(); });
  }

  if (keyWord.status === PsychoJS.Status.STARTED) {
    let theseKeys = keyWord.getKeys({keyList: ['y', 'n'], waitRelease: false});
    
    // check for quit:
    if (theseKeys.length > 0 && theseKeys[0].name === 'escape') {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      keyWord.keys = theseKeys[0].name;  // just the last key pressed
      keyWord.rt = theseKeys[0].rt;
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of testTrialComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function testTrialRoutineEnd() {
  //------Ending Routine 'testTrial'-------
  for (const thisComponent of testTrialComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  psychoJS.experiment.addData('keyWord.keys', keyWord.keys);
  if (typeof keyWord.keys !== undefined) {  // we had a response
      psychoJS.experiment.addData('keyWord.rt', keyWord.rt);
      routineTimer.reset();
      }
  
  keyWord.stop();
  // the Routine "testTrial" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var endScreenComponents;
function endScreenRoutineBegin() {
  //------Prepare to start Routine 'endScreen'-------
  t = 0;
  endScreenClock.reset(); // clock
  frameN = -1;
  routineTimer.add(20.000000);
  // update component parameters for each repeat
  // keep track of which components have finished
  endScreenComponents = [];
  endScreenComponents.push(textEnd);
  
  for (const thisComponent of endScreenComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function endScreenRoutineEachFrame() {
  //------Loop for each frame of Routine 'endScreen'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = endScreenClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *textEnd* updates
  if (t >= 0.0 && textEnd.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    textEnd.tStart = t;  // (not accounting for frame time here)
    textEnd.frameNStart = frameN;  // exact frame index
    textEnd.setAutoDraw(true);
  }

  frameRemains = 0.0 + 20 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (textEnd.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    textEnd.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of endScreenComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function endScreenRoutineEnd() {
  //------Ending Routine 'endScreen'-------
  for (const thisComponent of endScreenComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  return Scheduler.Event.NEXT;
}


function endLoopIteration({thisScheduler, isTrials=true}) {
  // ------Prepare for next entry------
  return function () {
    // ------Check if user ended loop early------
    if (currentLoop.finished) {
      // Check for and save orphaned data
      if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
        psychoJS.experiment.nextEntry();
      }
      thisScheduler.stop();
    } else if (isTrials) {
      psychoJS.experiment.nextEntry();
    }
  return Scheduler.Event.NEXT;
  };
}


function importConditions(loop) {
  const trialIndex = loop.getTrialIndex();
  return function () {
    loop.setTrialIndex(trialIndex);
    psychoJS.importAttributes(loop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});

  return Scheduler.Event.QUIT;
}
