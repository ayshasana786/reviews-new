import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import streamlit as st
import pickle
from sklearn.model_selection import train_test_split

# Read our dataset using read_csv()
bbc_text = pd.read_csv('bbc-text.txt')
bbc_text=bbc_text.rename(columns = {'text': 'News_Headline'}, inplace = False)
bbc_text.head()
bbc_text.category = bbc_text.category.map({'tech':0, 'business':1, 'sport':2, 'entertainment':3, 'politics':4})
bbc_text.category.unique()
from sklearn.model_selection import train_test_split
X = bbc_text.News_Headline
y = bbc_text.category
#split data
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.6, random_state = 1)
vector = CountVectorizer(stop_words = 'english',lowercase=False)
# fit the vectorizer on the training data
vector.fit(X_train)
vector.vocabulary_
X_transformed = vector.transform(X_train)
X_transformed.toarray()
# for test data
X_test_transformed = vector.transform(X_test)
from sklearn.naive_bayes import MultinomialNB
naivebayes = MultinomialNB()
naivebayes.fit(X_transformed, y_train)
from sklearn.metrics import classification_report
print(classification_report(naivebayes.predict(X_test_transformed), y_test))
headline1 = ['Portugal crash out of FIFA World Cup 2022, Ronaldo in tears']
vec = vector.transform(headline1).toarray()
print('Headline:', headline1)
headline1 = ['Portugal crash out of FIFA World Cup 2022, Ronaldo in tears']
vec = vector.transform(headline1).toarray()
print('Headline:', headline1)
print(str(list(naivebayes.predict(vec))[0]).replace('0', 'TECH').replace('1', 'BUSINESS').replace('2', 'SPORTS').replace('3','ENTERTAINMENT').replace('4','POLITICS'))
headline1 = ['There will be recession throughout the world as predicted by world bank']
vec = vector.transform(headline1).toarray()
print('Headline:', headline1)
print(str(list(naivebayes.predict(vec))[0]).replace('0', 'TECH').replace('1', 'BUSINESS').replace('2', 'SPORTS').replace('3','ENTERTAINMENT').replace('4','POLITICS'))
import pickle

saved_model = pickle.dumps(naivebayes)
s = pickle.loads(saved_model)
headline1 = ['There will be recession throughout the world as predicted by world bank']
vec = vector.transform(headline1).toarray()

s.predict(vec)[0]
