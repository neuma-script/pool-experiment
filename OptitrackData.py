import pandas as pd

file1 = open("optitrack.csv", "r")
allLines = file1.readlines()
allLines = allLines[7::]
df_output = pd.DataFrame(columns = ['Ball #', 'Dist.', 'Proximity'])
count = 6
outputRows = 0
for item in allLines:
	itemList = item.split(",")
	#x:2 ; y: 3; z: 4; 
	if (count >= len(itemList)):
		break
	if (-0.01 < float(itemList[count]) < 0.01):
		if (float(itemList[count + 2]) < 1 and float(itemList[count + 2]) > -1):
			proximity = "Hit"
		elif (float(itemList[count + 2]) < 150 and float(itemList[count + 2]) > -150):
			proximity = "Close"
		elif (float(itemList[count + 2]) < 350 and float(itemList[count + 2]) > -350):
			proximity = "Medium"
		else:
			proximity = "Off Target"

		df_output.loc[outputRows] = [outputRows + 1, itemList[count + 2], proximity]
		outputRows += 1
		count += 7

df_output.to_excel("BallPositions.xlsx", sheet_name = 'temp', index = False)
print("complete")
