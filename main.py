import nltk, re, pprint
import text_labelling as label
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter



#define path
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'files')

#label.initialize()
token_dict = label.walk_path(filename)
# tfidf = TfidfVectorizer(tokenizer=label.tokenize, stop_words='english')
# tfs = tfidf.fit_transform(token_dict.values())

# feature_names = tfidf.get_feature_names()
# for col in tfs.nonzero()[1]:
#     print (feature_names[col], ' - ', tfs[0, col])

for file in token_dict:
	tokens = label.tokenize(file)
	count = Counter(tokens)
	print (count.most_common(10))
