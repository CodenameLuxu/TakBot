

import os
import nltk
from nltk import WordNetLemmatizer
from multiprocessing import Pool
import spacy
# nltk.download()


class NLPEngine:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.nlp = spacy.load("en_core_web_sm")

    def lemmize(self,text, cores=6): # tweak cores as needed
        # text = text.split()
        # lemmatized_output = [self.lemmatizer.lemmatize(w) for w in text]
        # with Pool(processes=cores) as pool:
        #     wnl = WordNetLemmatizer()
        #     result = pool.map(wnl.lemmatize, text)
        return lemmatized_output

    def tokenize(self,sentence):
        keep = ["VERB" , "ADJ", "PRON","CCONJ","NOUN"]
        doc = self.nlp(sentence)
        tokens =  [token for token in doc if token.pos_ in keep ]
        # print([token.pos_ for token in tokens])
        return tokens


    def terminatewords(self):
        words = ['end','x','bye','goodnight','terminate']
        return words

    def isTerminateword(self,key):
        words = self.terminatewords()
        return key in words
