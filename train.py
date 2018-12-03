

import logging
import os.path
import sys
import multiprocessing
from gensim.corpora import WikiCorpus
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

if __name__ == '__main__':
    rdata="zhwiki_simple2.txt"
    modelpath="train.model"
    model=Word2Vec(LineSentence(rdata),size=400,window=5,min_count=5,workers=multiprocessing.cpu_count())
    model.save(modelpath)