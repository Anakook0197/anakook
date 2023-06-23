from bs4 import BeautifulSoup
import requests
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

url = 'https://www.britannica.com/'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
meta_tags = soup.find_all('meta')

title = ''
description = ''
keywords = []

for tag in meta_tags:
   title = tag.attrs
description = tag.attrs
print('Title:', title)
print('Description:', description)

content = soup.get_text()
print(content)
tokens = word_tokenize(content)
filtered_tokens = [token.lower()for token in tokens if token.lower() not in stop_words]
print(filtered_tokens)
stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
print(stemmed_tokens)
preprocessed_content = ''.join(stemmed_tokens)

print('Title:', title)
print('Description:', description)
print('Preprocessed content:', preprocessed_content[0:400])



