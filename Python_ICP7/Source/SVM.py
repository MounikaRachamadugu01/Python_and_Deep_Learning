"""
1. Change the classifier in the given code to
    a. SVM and see how accuracy changes
    b. change the tfidfvectorizer to use bigram and see how the accuracy changes
       TfidfVectorizer(ngram_range=(1,2))
    c. Set argument stop_words='english'and see how accuracy changes
"""

from sklearn.datasets import fetch_20newsgroups
from sklearn.svm import SVC, LinearSVC
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB

# Using Naive Bayes classifier
tfidf_Vect = TfidfVectorizer()
twenty_train = fetch_20newsgroups(subset='train', shuffle=True)
X_train_tfidf = tfidf_Vect.fit_transform(twenty_train.data)
twenty_test = fetch_20newsgroups(subset='test', shuffle=True)
X_test_tfidf = tfidf_Vect.transform(twenty_test.data)
nb_clf = MultinomialNB()
nb_clf.fit(X_train_tfidf, twenty_train.target)
predict = nb_clf.predict(X_test_tfidf)
score = metrics.accuracy_score(twenty_test.target, predict)
print("Score with Naive Bayes Classifier: ", score*100)

# Using SVM classifier
svm_clf = SVC(kernel='linear')
svm_clf.fit(X_train_tfidf, twenty_train.target)
predict = svm_clf.predict(X_test_tfidf)
score = metrics.accuracy_score(twenty_test.target, predict)
print("\n Score with SVM Classifier: ", score*100)

# Changing the tfidf vectorizer
twenty_train = fetch_20newsgroups(subset='train', shuffle=True)
tfidf_Vect = TfidfVectorizer(ngram_range=(1, 2))
X_train_tfidf = tfidf_Vect.fit_transform(twenty_train.data)
nb_clf = MultinomialNB()
nb_clf.fit(X_train_tfidf, twenty_train.target)
twenty_test = fetch_20newsgroups(subset='test', shuffle=True)
X_test_tfidf = tfidf_Vect.transform(twenty_test.data)
predict = nb_clf.predict(X_test_tfidf)
score = metrics.accuracy_score(twenty_test.target, predict)
print("\n Score after changing the tfidf vectorizer: ", score*100)

# Set argument stop_words='english' to determine the accuracy
twenty_train = fetch_20newsgroups(subset='train', shuffle=True)
tfidf_Vect = TfidfVectorizer(stop_words='english')
X_train_tfidf = tfidf_Vect.fit_transform(twenty_train.data)
nb_clf = MultinomialNB()
nb_clf.fit(X_train_tfidf, twenty_train.target)
twenty_test = fetch_20newsgroups(subset='test', shuffle=True)
X_test_tfidf = tfidf_Vect.transform(twenty_test.data)
predict = nb_clf.predict(X_test_tfidf)
score = metrics.accuracy_score(twenty_test.target, predict)
print("\n Score after setting an argument stop_words = 'english' : ", score*100)








