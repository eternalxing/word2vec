from gensim.models import Word2Vec

model = Word2Vec.load('train.model')

print(model.most_similar(u'中国', topn=20))

