import winsound, time, datetime

# Need to get a beep that is 500ms long this one is about 1000ms long
def normalTrial():
	beforeBeep1 = str(datetime.datetime.now().time())
	winsound.PlaySound("Fuzzy Beep-SoundBible.com-1580329899", winsound.SND_FILENAME)
	# print("Right After Beep: " + str(datetime.datetime.now().time()))
	time.sleep(2)
	beforeBeep2 = str(datetime.datetime.now().time())
	winsound.PlaySound("Fuzzy Beep-SoundBible.com-1580329899", winsound.SND_FILENAME)
	time.sleep(1)
	# Hitting action occurs in that 1000ms
	time.sleep(2)
	# Positioning occurs in the 20000ms
	return [beforeBeep1, beforeBeep2]
	

def visualTrial():
	beforeBeep1 = str(datetime.datetime.now().time())
	winsound.PlaySound("Fuzzy Beep-SoundBible.com-1580329899", winsound.SND_FILENAME)
	# print("Right After Beep: " + str(datetime.datetime.now().time()))
	time.sleep(1)
	#Visual Stimuli for 500ms 
	time.sleep(0.5)
	# print(str(datetime.datetime.now().time()))
	beforeBeep2 = str(datetime.datetime.now().time())
	winsound.PlaySound("Fuzzy Beep-SoundBible.com-1580329899", winsound.SND_FILENAME)
	time.sleep(1)
	#Hitting action occurs
	time.sleep(2)
	# Positioning occurs
	# print(str(datetime.datetime.now().time()))
	return [beforeBeep1, beforeBeep2]


def kinestheticTrial():
	beforeBeep1 = str(datetime.datetime.now().time())
	winsound.PlaySound("Fuzzy Beep-SoundBible.com-1580329899", winsound.SND_FILENAME)
	# print("Right After Beep: " + str(datetime.datetime.now().time()))
	time.sleep(1)
	#Kinesthetic Stimuli for 500ms 
	time.sleep(0.5)
	# print(str(datetime.datetime.now().time()))
	beforeBeep2 = str(datetime.datetime.now().time())
	winsound.PlaySound("Fuzzy Beep-SoundBible.com-1580329899", winsound.SND_FILENAME)
	time.sleep(1)
	#Hitting action occurs
	time.sleep(2)
	# Positioning occurs
	# print(str(datetime.datetime.now().time()))
	return [beforeBeep1, beforeBeep2]


kinestheticTrial()