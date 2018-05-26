import nltk, re, pprint
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
import string
import os
from nltk.stem.porter import *



def initialize():
	nltk.download()
	


def create_raw(document):
    lowers = document.lower()
    #remove the punctuation using the character deletion step of translate
    no_punctuation = lowers.translate(str.maketrans('','',string.punctuation))
    return no_punctuation

def tokenize(text):
	tokens = nltk.word_tokenize(text)
	new_tokens = remove_stopwords(tokens)
	stemmer = PorterStemmer()
	stems = stem_tokens(new_tokens, stemmer)
	return stems

def remove_stopwords(tokens):
	filtered = [w for w in tokens if not w in stopwords.words('english')]
	return filtered

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def walk_path(path):
	token_dict = []
	for subdir, dirs, files in os.walk(path):
		for file in files:
			file_path = subdir + os.path.sep + file
			raw = open(file_path, 'r')
			raw = raw.read()
			text = create_raw(raw)
			token_dict.append(text)
	return token_dict







