# from gensim.models.wrappers import FastText

# # model = FastText.load_fasttext_format('wiki.simple')

# # print(model.most_similar('teacher'))

import gensim


model = gensim.models.KeyedVectors.load_word2vec_format('lexvec.enwiki+newscrawl.300d.W.pos.vectors', binary=False)
# if you vector file is in binary format, change to binary=True
labels = ["advocacy","animal","art","community","child","mentoring","food","environmental","heath","garden","office","sports","fundraising","event"]

for word in labels:
	try:
		print(model.wv.most_similar(positive=word))
	except:
		print(word+"doesn't exist in word2vec")
		pass

print("female and male similarity")
print (model.wv.similarity('female', 'male'))