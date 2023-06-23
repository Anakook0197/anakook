import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

spam_df = pd.read_csv('spam_data.csv')

X_train, X_test, y_train, y_test = train_test_split(spam_df['text'], spam_df['label'], test_size=0.2,
random_state=42)

# Vectorize the text data using a Bag of Words model
vectorizer = CountVectorizer()
X_train_vect = vectorizer.fit_transform(X_train)
X_test_vect = vectorizer.transform(X_test)

# Train a Multinomial Naive Bayes classifier
clf = MultinomialNB()
clf.fit(X_train_vect, y_train)

accuracy = clf.score(X_test_vect, y_test)
print("Accuracy: {:.2f}%".format(accuracy*100))

new_message = [input("Enter your text data\n")]
new_message_vect = vectorizer.transform(new_message)
prediction = clf.predict(new_message_vect)
if(prediction[0]=="spam"):
   print("Your message is a spam")
else:
   print("Your message is genuine")
