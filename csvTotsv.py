import pandas as pd
from glob import glob
import re, os

os.chdir('./temp')
for file in glob('*.csv'):
	input_file = file
	output_file = re.sub(r'\.csv', '.tsv', str(file))

	df = pd.read_csv(input_file, error_bad_lines=False)
	allRows = df.iloc[:].values

	f = open(output_file, 'w')
	for item in allRows:
		for subItem in item:
			f.write(str(subItem))
			f.write('\t')
		f.write('\n')

	f.close()