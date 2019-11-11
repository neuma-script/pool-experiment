from psychopy import core, visual

def showText(win, myText):
    message = visual.TextStim(win, text = myText)
    message.draw()
    win.flip()
    core.wait(1.0)
    win.close()
    core.quit()