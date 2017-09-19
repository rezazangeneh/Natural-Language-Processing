import textacy
import re
from nltk import PorterStemmer
from remSF import remSF



def remSW(text):
	with open ('stopWords.txt') as f:
		stopWords = f.read().split()

	text1 = " ".join(word for word in text.split() if word not in stopWords)

	return text1

def preProcess(text):
	#text = textacy.preprocess.fix_bad_unicode(text, normalization=u'NFC')
	text = text.lower()
	text = remSF(text)
	text = re.sub(r'[^\x00-\x7f]', ' ', text)
	text = re.sub(r'(\@(.)*\s)',' ', text)
	#text = re.sub(r'(\#)((.)*)\2(\s)',r' \2', text)
	text = re.sub(r'\,|\(|\)|\@|\$|\.', ' ' ,text)
	text = re.sub(r'([a-z])\1{2,}', r'\1', text)

	text = textacy.preprocess.normalize_whitespace(text) #\n \t \s
	text = textacy.preprocess.unpack_contractions(text) #Mr they've they have
	text = textacy.preprocess.remove_accents(text, method=u'unicode')	
	text = textacy.preprocess.remove_punct(text, marks=None)
	text = textacy.preprocess.replace_numbers(text, replace_with=u'some_number')
	text = re.sub(r'(\s)+.(\s)+',' ',text)
	print text
	return text

def normalize(text):
	ps = PorterStemmer()
	text1=""
	for word in text.split():
		text1 += ps.stem(word)
		text1 += " " 

	return text1

def processTweets(text):
	return normalize(remSW(preProcess(remSF(text))))