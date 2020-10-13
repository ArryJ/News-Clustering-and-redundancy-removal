# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 23:10:54 2020

@author: ajain
"""
import pandas as pd
import nltk
import string

articles = []
for j in range (1,4);
    k = 32
    if (j==2):
        k=30
    for i in range(1,k):
        s1 = str(j) + "_" + str(i) + "_P.csv"
        s2 = str(i) + "_TH.csv"
        s3 = str(i) + "_TOI.csv"
        dataP = pd.read_csv(s1)
        dataTH = pd.read_csv(s2)
        dataTOI = pd.read_csv(s3)
        for j in range(0,len(dataP)):
            articles.append(dataP['Article'][j])
        for j in range(0,len(dataTH)):
            articles.append(dataTH['Content'][j])
        for j in range(0,len(dataTOI)):
            articles.append(dataTOI['Content'][j])

dataTH = pd.read_csv("1_TH.csv")
dataTOI = pd.read_csv("1_TOI.csv")

# 

# for i in range(0,len(dataP)):
#     articles.append(dataP['Article'][i])

for i in range(len(dataTH)):
    articles.append(dataTH['Content'][i])

for i in range(len(dataTOI)):
    articles.append(dataTOI['Content'][i])

for i in range(len(articles)):
    if  type(articles[i]) is not str:
           del articles[i]
   
    articles[i] = articles[i].lower()

print(type(articles))

# for i in range(len(articles)):
#     articles[i] = articles[i].translate(str.maketrans('','' , string.punctuation))
    

# for i in range(len(articles)):
#     articles[i] = " ".join(articles[i].split())





# from nltk import word_tokenize
# words = []

# for i in range(len(articles)):
#     words.append(word_tokenize(articles[i]))


# from nltk.corpus import stopwords

# stop_words = set(stopwords.words("english"))


# for i in range(len(words)):
#     words[i] = [word for word in words[i] if word not in stop_words]  
    


# for i in range(len(words)):
#     words[i] = [token for token in words[i] if not token.isnumeric()]   
    
# for i in range(len(words)):    
#     words[i] = [token for token in words[i] if len(token) > 1]

    
# from nltk.stem.wordnet import WordNetLemmatizer

# lemmatizer = WordNetLemmatizer()
  

# for i in range(len(words)):
#     words[i] = [lemmatizer.lemmatize(j) for j in words[i]]

# from gensim.models import Phrases

# bigram = Phrases(words, min_count=20)

# for idx in range(len(words)):
#     for token in bigram[words[idx]]:
#         if '_' in token:
#             # Token is a bigram, add to document.
#             words[idx].append(token)    


# from gensim.corpora import Dictionary

# dictionary = Dictionary(words)
# dictionary.filter_extremes(no_below = 20, no_above=0.5)


# corpus = [dictionary.doc2bow(doc) for doc in words]

# from gensim.models import LdaModel
# num_topics = 10
# chunksize = 1500
# passes = 20
# iterations = 400
# eval_every = None

# temp = dictionary[0]

# id2word = dictionary.id2token

# model = LdaModel(
#     corpus=corpus,
#     id2word=id2word,
#     chunksize=chunksize,
#     alpha='auto',
#     eta='auto',
#     iterations=iterations,
#     num_topics=num_topics,
#     passes=passes,
#     eval_every=eval_every
# )

# top_topics = model.top_topics(corpus)


# from pprint import pprint
# pprint(top_topics)

# import pyLDAvis.gensim

# lda_display = pyLDAvis.gensim.prepare(model, corpus, dictionary, sort_topics=True)
# pyLDAvis.display(lda_display)
