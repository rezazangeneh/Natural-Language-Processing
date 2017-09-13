import re

  
def preprocess(text, removeNum = 0, removePunct = 0, removeStopWords = 0, removeCussWords = 0, encode = ''):
	#remove non-ascii characters
	text = re.sub(r'[^\x00-\x7f]' , ' ', text)

	keyPunct1 = re.compile(r'\~|\#|\@|\$|\%|\^|\{|\}|\[|\]|\:|\;|\/|\`|\*|\(|\)')
	keyPunct2 = re.compile(r'\,|\.|!|\'|\"')

	#remove numerical data
	# 0: don't remove
	# 1: remove basic numbers ex. xxxx 789 xxxx will be removed, 7xx98 won't
	# 2: remove all numbers  
	if removeNum:
		text = re.sub(r'[^a-zA-Z]+[0-9\.\,]+[^a-zA-Z]+', ' ', text)
		if removeNum == 2:
			text = re.sub(r'[0-9]',' ',text)

	# removePunct = 0 : No removal
	# removePunct = 1 : Basic removal, preserve , . ! ' "
	# removePunct = 2 : Extreme, remove all
	if removePunct:
		text = re.sub(keyPunct1, ' ',text)
		if removePunct == 2:
			text = re.sub(keyPunct2, ' ',text)

	#Remove words present in stopWords.txt
	if removeStopWords:
		stopWordsFile = 'stopWords.txt'
		text = " ".join(word for word in text.split() if word not in open(stopWordsFile).read())

	#Remove words present in cussWords.txt
	if removeCussWords:
		cussWordsFile = 'cussWords.txt'
		text = " ".join(word for word in text.split() if word not in open(cussWordsFile).read())

	#encode in the given encoding, eg. UTF-8, UTF-7, etc
	if encode:
		text = text.encode(encode)

	text = re.sub(r'(\s)+', ' ', text)
	return text

while 1:
	file = raw_input("Choose a file: ")
	text = open(file).read()
	print preprocess(text,):