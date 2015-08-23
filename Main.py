# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 13:49:30 2015
@author: arkag
"""
import pandas as panda
import string
from nltk.tokenize import word_tokenize 
import easygui
import re
import nltk
from sklearn.externals import joblib
from nltk.util import ngrams
#nltk.download('punkt')


def import_file():
    filepath = easygui.fileopenbox()
    #"C:\\Users\\arkag\\Desktop\\Akosha\\as.txt"
    lines = open(filepath,'r').readlines()
    return lines
    

def data_clean(fileloaded,val):
    if val == "Model":
        new_format = [filter(lambda x: x in string.printable, (re.sub(r"(?:\@|https?\://)\S+", "", line)).lower().translate(None, string.punctuation)) for line in fileloaded]
    else:
        new_format = filter(lambda x: x in string.printable, (re.sub(r"(?:\@|https?\://)\S+", "", fileloaded)).lower().translate(None, string.punctuation))
    #print lines
    return new_format
    
def tokenize(data,val):
    if val == "Model":
        tokenize_data = [word_tokenize(vals) for vals in data[0]]
    else:
        tokenize_data = word_tokenize(data)
    return tokenize_data

def create_model(tokenized_data):
    tokens_list = [tokens  for ndata in tokenized_data for tokens in ndata]   
    cfreq_data_bigram = nltk.ConditionalFreqDist(nltk.bigrams((tokens_list)))
    n = 3
    trigrams = ngrams(tokens_list, n)
    z = 4
    m = 5
    n = 6
    fourgram = ngrams(tokens_list, z)
    fivegram = ngrams(tokens_list, m)
    sixgram = ngrams(tokens_list, n)
    return cfreq_data_bigram,trigrams,fourgram,fivegram,sixgram


def main():
    val="Model"
    #select file containing tweets and remove hyperlinks to use for training the corpus 
    fileloaded = import_file()
    corpus_data = panda.DataFrame(data_clean(fileloaded,val))
    # remove duplicate values to make it a more stable unbiased corpus
    new_corpus = corpus_data.drop_duplicates()
    print new_corpus
    joblib.dump(new_corpus,"Dataset.pkl")
    tokenized_data = tokenize(new_corpus,val)
    print tokenized_data
    bigram_model,trigram_model,fourgram_model,fivegram_model,sixgram_model = create_model(tokenized_data)
    joblib.dump(bigram_model,"Bigram.pkl")
    joblib.dump(list(trigram_model),"Trigram.pkl")
    joblib.dump(list(fourgram_model),"Fourgram.pkl")
    joblib.dump(list(fivegram_model),"Fivegram.pkl")
    joblib.dump(list(sixgram_model),"Sixgram.pkl")
    
    

if __name__ == "__main__":
    main()
