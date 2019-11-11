# Author: Varunil N. Shah
# This first for loop is for all the runs in the experinment 
import random, datetime, functions
import pandas as pd
visualTrial = True
kinesticTrial = True


for runNumber in range(1, 3):
	runTime = str(datetime.datetime.now().time())
	df_output = pd.DataFrame(columns = ['Run Number', 'Run Time', 'Group Name', 'Position Number', 'Trial Number', 'Trial Type', 'First Beep', 'Second Beep'])
	currentTrial = 1
	i = 0
	groupName = ''
	times = []
	trialType = ''
	positionNumber1 = 1
	positionNumber2 = 2
# This is to put a name to each group
	for groupNum in range(5):
		if groupNum == 0:
			groupName = 'Left Corner'
		elif groupNum == 1:
			groupName = 'Left Middle'
		elif groupNum == 3:
			groupName = 'Right Middle'
		elif groupName == 4:
			groupName = 'Right Corner' 
		
		# This is to help Randomize 
		possibleTrials = [0, 1, 2, 3, 4, 5, 6]
		visualTrialNumber = random.choice(possibleTrials)
		possibleTrials.remove(visualTrialNumber)
		kinesticTrialNumber = random.choice(possibleTrials)
		# Special Case if it is the Middle Middle group
		if (groupNum == 2):
			groupName = 'Middle Middle'
			possibleTrials.remove(kinesticTrialNumber)
			visualTrialNumber2 = random.choice(possibleTrials)
			possibleTrials.remove(visualTrialNumber2)
			kinesticTrialNumber2 = random.choice(possibleTrials)
			# This is to go through the 6 trials in each group
			for trialNumber in range(6):
				# print("Run " + str(runNumber) + "Trial " + str(currentTrial) + "Time: " + str(datetime.datetime.now().time()))
			
				if trialNumber == visualTrialNumber or trialNumber == visualTrialNumber2:
					trialType = "Visual"
					times = functions.visualTrial()
				elif trialNumber == kinesticTrialNumber or trialNumber == kinesticTrialNumber2:
					trialType = 'Kinestic'
					times = functions.kinestheticTrial()
				else:
					trialType = "Normal"
					times = functions.normalTrial()
				if trialNumber <= 2:
					df_output.loc[i] = [runNumber, runTime, groupName, positionNumber1, currentTrial, trialType, times[0], times[1]]
				else:
					df_output.loc[i] = [runNumber, runTime, groupName, positionNumber2, currentTrial, trialType, times[0], times[1]]
				currentTrial = currentTrial + 1
				i = i + 1
			positionNumber1 = positionNumber2 + 1
			positionNumber2 = positionNumber2 + 2
			# Do two of visual and kinestic Trial 
		# This is the normal case for all groups
		else:
			# THis is to go though 6 trials per group
			for trialNumber in range(6):
				# print("Run " + str(runNumber) + "Trial " + str(currentTrial) + "Time: " + str(datetime.datetime.now().time()))
				if trialNumber == visualTrialNumber:
					trialType = "Visual"
					times = functions.visualTrial()
				elif trialNumber == kinesticTrialNumber:
					trialType = 'Kinestic'
					times = functions.kinestheticTrial() 
				else:
					trialType = "Normal"
					times = functions.normalTrial()
				if trialNumber <= 2:
					df_output.loc[i] = [runNumber, runTime, groupName, positionNumber1, currentTrial, trialType, times[0], times[1]]
				else:
					df_output.loc[i] = [runNumber, runTime, groupName, positionNumber2, currentTrial, trialType, times[0], times[1]]
				currentTrial = currentTrial + 1
				i = i + 1
			positionNumber1 = positionNumber2 + 1
			positionNumber2 = positionNumber2 + 2
			# Do one of visual and kinestic trial 
	# df_beingadded = pd.pivot_table(df_output, index = ['runNumber', 'runTime'], columns = ['groupName', 'currentTrial', 'trialType', 'times[0]', 'times[1]']) 
	df_output.to_excel("output.xlsx", sheet_name = 'temp', index = False)
	# output_table1 = pd.pivot_table(df_output, columns = ['Group Name', 'Trial Number', 'Trial Type', 'First Beep', 'Second Beep'])
	# with pd.ExcelWriter('Pool_Data.xlsx') as writer:
	# 	output_table1.to_excel(writer, sheet_name = 'Run ' + str(runNumber))
