import nltk, re, pprint
import text_labelling as label
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter
import gensim




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

top_words=[]


for file in token_dict:
	tokens = label.tokenize(file)
	count = Counter(tokens)
	words = []
	for (key,value) in count.most_common(10):
		words.append(key)
	top_words.append(words)


model = gensim.models.KeyedVectors.load_word2vec_format('lexvec.enwiki+newscrawl.300d.W.pos.vectors', binary=False)
# if you vector file is in binary format, change to binary=True
labels = ["animal","art","communication","child","teach","food","environment","health","garden","sport","disability","technology","festival"]
labels_count = [0] * len(labels)

count = 0
for candidates in top_words:
	max_score = 0.0
	final_label = -1
	for choice in candidates:
		for i in range (0,len(labels)):
			try:
				word = labels[i]
				score = model.wv.similarity(choice,word)
				if(score>max_score):
					max_score = score
					final_label = i
			except:
				pass
	print ("for file " + str(count) + " the closest label is    " + labels[final_label])
	labels_count[final_label] = labels_count[final_label] + 1
	count = count + 1

for i in range(0,len(labels)):
	print ("category: " + labels[i] + " has " + str(labels_count[i]) + " labels " )


