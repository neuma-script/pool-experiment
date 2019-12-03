import pandas as pd

file1 = open("eye.csv", "r")
allLines = file1.readlines()
allLines = allLines[1::]
df_output = pd.DataFrame(columns = ["Time", "horz_gaze_coord", "vert_gaze_coord"])
outputRows = 0
for item in allLines:
	itemList = item.split(",")
	df_output.loc[outputRows] = [itemList[3], itemList[7], itemList[8]]
	outputRows += 1

df_output.to_excel("eyeData.xlsx", sheet_name = 'temp', index = False)
print("complete")