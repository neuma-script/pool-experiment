import pandas as pd

file1 = open("optitrack.csv", "r")
allLines = file1.readlines()
allLines = allLines[7::]
df_output = pd.DataFrame(columns = ['Ball #', 'Dist.'])
count = 6
outputRows = 0
for item in allLines:
	itemList = item.split(",")
	#x:2 ; y: 3; z: 4; 
	if (itemList[count] != "" and -0.01 < float(itemList[count]) < 0.01):
		df_output.loc[outputRows] = [outputRows + 1, itemList[count + 2]]
		outputRows += 1
		count += 4

df_output.to_excel("positions.xlsx", sheet_name = 'temp', index = False)
print("complete")
