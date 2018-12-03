
import multiprocessing
import codecs
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence


if __name__ == '__main__':
    fname="zhwiki_simple2.txt"
    f=codecs.open(fname,encoding='gbk')
    print(f)
    rdata="zhwiki_simple2.txt"
    modelpath="train.model"
    model=Word2Vec(LineSentence(f),size=400,window=5,min_count=5,workers=multiprocessing.cpu_count())
    model.save(modelpath)