import textacy
from textPreProc import preprocess
import en_core_web_sm
import spacy


def getPhrases(text, op_file='Output.txt', min_ngrams = 1, max_ngrams = 1, topn = 10):
	
	#text = open(file).read()
	text = preprocess(text.decode('utf-8'))
	#text = nltk.word_tokenize(text.decode('utf-8'))

	#print text
	nlp = spacy.load('en_core_web_sm')
	doc = nlp(text)

	
	op = open(op_file,"a")
	op.write("Value: %s" %file)
	op.write('\n\nKey Terms:\n')
	
	for i in range(min_ngrams,max_ngrams):
		keyp = list(textacy.extract.ngrams(doc, i, filter_stops=True, filter_punct=True, filter_nums=True))[:topn]
		op.write(str(keyp))
		op.write('\n')
	op.write('\n\n\n')
	op.close()
	
'''	
while(1):
	file = raw_input("Enter text: ")
	op_file = raw_input("Enter name of output file: ")
	getPhrases(file, op_file,min_ngrams = 1, max_ngrams = 5, topn = 10)
'''	