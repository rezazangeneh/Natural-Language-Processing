#Pre Processing Text Files, Varun Chitale 08/17/2017

import nltk
import re
from nltk.stem import PorterStemmer
import textacy


def preprocess(text):

	text = textacy.preprocess.fix_bad_unicode(text, normalization=u'NFC')
	text = textacy.preprocess.normalize_whitespace(text)
	text = textacy.preprocess.remove_accents(text, method=u'unicode')
	text = textacy.preprocess.remove_punct(text, marks=None)
	text = textacy.preprocess.replace_numbers(text, replace_with=u'some_number')
	text = re.sub(r'(\s\.\s)',' ',text)

	return text