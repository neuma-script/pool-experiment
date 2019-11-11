
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# My functions.
  
from psychopy import core, visual, event
import time
import varunil


win = visual.Window([400,300], fullscr = True, monitor = 'testmonitor')

for i in range (10):
    core.wait(1.0)
    win.flip()
    varunil.debugLog(i)
    
win.close()
core.quit()

