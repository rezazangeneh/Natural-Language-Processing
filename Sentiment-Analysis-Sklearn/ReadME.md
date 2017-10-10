Sentiment Analysis using Sklearn's feature extraction.
CountVectorizer
TfIdfVectorizer

Accuracy ~ 90%

The trick is to limit the training data to a suitable number of examples in order to eliminate the risk of overfitting,
while making sure that too less examples will result in underfitting.
A shuffle on the data available is generally a good idea; when the example isn't one of time-series 
