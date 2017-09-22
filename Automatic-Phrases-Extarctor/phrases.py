import nltk
import pandas
import re
import string
from collections import Counter
from nltk.util import ngrams 
import json

non_speaker = re.compile('[A-Za-z]+: (.*)')
data={}


def untokenize(ngram):
	tokens = list(ngram)
	return "".join([" "+i if not i.startswith("'") and \
							 i not in string.punctuation and \
							 i != "n't"
						  else i for i in tokens]).strip()


def extract_phrases(text, phrase_counter, length):
	global data
	for sent in nltk.sent_tokenize(text):

		strip_speaker = non_speaker.match(sent)
		if strip_speaker is not None:
			sent = strip_speaker.group(1)
		words = nltk.word_tokenize(sent)
		for phrase in ngrams(words, length):
			if all(word not in string.punctuation for word in phrase):
				phrase_counter[untokenize(phrase)] += 1 


	#print phrase_counter.most_common(50)
	needed_list = phrase_counter.most_common(50)
	data['%d-grams'%length] = needed_list
	
def getPhrases(text):
	global data
	if text == ''
		text = open('NTSCData').read()
	phrase_counter1 = Counter()
	extract_phrases(text,phrase_counter1,1)
	phrase_counter2 = Counter()
	extract_phrases(text,phrase_counter2,2)
	phrase_counter3 = Counter()
	extract_phrases(text,phrase_counter3,3)
	data['Total_Words'] = len(nltk.word_tokenize(text))
	#print json.dumps(data)
	data1 = json.dumps(data)
	return data1

'''
data1 = getPhrases()
print data1
'''