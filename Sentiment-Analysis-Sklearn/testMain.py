#import gensim, nltk
import pandas as pd
#import numpy as np
#import tensorflow as tf
#from textPreProc import normalize, basicReplacement
#from sklearn import preprocessing
import os #, glob


os.environ['TF_CPP_MIN_LOG_LEVEL']='2'


#Training Data
df = pd.read_csv('finalData.csv', delimiter='\t')
sent = df['Sentence'].values.tolist()
labels = df['Sentiment'].values.tolist()


cut = 1000
sent1 = sent[:cut]
labels1 = labels[:cut]
sent2 = sent[cut:]
labels2 = labels[cut:]


#train_input = np.zeros((len(sent1),size_features))
#train_output = np.zeros((len(sent1), 2))


from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer

vectorizer = TfidfVectorizer()
#vectorizer = CountVectorizer()

train_input = vectorizer.fit_transform(sent1)
train_output = labels1
	
#print train_input,train_output
#print np.shape(train_input)
#print np.shape(train_output)
#print (train_input,train_output)

test_input = vectorizer.transform(sent2)
test_output = labels2


from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier


lr_clf = LogisticRegression()
lr_clf.fit(train_input, train_output)

rfc_clf = RandomForestClassifier(criterion='entropy')
rfc_clf.fit(train_input, train_output)


dt_clf = DecisionTreeClassifier()
dt_clf.fit(train_input, train_output)

print "Log Reg: ",lr_clf.score(test_input, test_output)
print "Random Forest: ",rfc_clf.score(test_input, test_output)
print "Decision Tree: ",dt_clf.score(test_input, test_output)

