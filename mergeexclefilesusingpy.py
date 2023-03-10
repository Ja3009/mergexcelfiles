import pandas as pd
import glob
path = r'test'
filenames = glob.glob(path + "\*.xlsx")
print('File names:', filenames)
finalexcelsheet = pd.DataFrame()
for file in filenames:
	df = pd.concat(pd.read_excel(
	file, sheet_name=None), ignore_index=True, sort=False)
	finalexcelsheet = finalexcelsheet.append(
	df, ignore_index=True)
print('Final Sheet:')
display(finalexcelsheet)

finalexcelsheet.to_excel(r'Final.xlsx', index=False)
