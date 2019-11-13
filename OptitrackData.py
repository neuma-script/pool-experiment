import pandas as pd

file1 = open("optitrack.csv", "r")
allLines = file1.readlines()
allLines = allLines[8::]
df_output = pd.DataFrame(columns = ['Ball #', 'Dist.'])
for item in allLines:
	itemList = item.split(",")
	#x:2 ; y: 3; z: 4; 
	print(itemList[2])
	if (itemList[2] != "" and -0.01 < float(itemList[2]) < 0.01):
		df_output.loc[0] = [1, itemList[3]]
		break

df_output.to_excel("positions.xlsx", sheet_name = 'temp', index = False)
