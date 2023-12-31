from __future__ import absolute_import, division, print_function
import pandas as pd
import numpy as np 
import string
import matplotlib.pyplot as plt 


import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.sequence import pad_sequences

from transformers import BertTokenizer
from transformers import TFAutoModel

from collections import Counter
import seaborn as sns 
import re
import os

from wordcloud import WordCloud
from nltk.corpus import stopwords
from fuzzywuzzy import process, fuzz

import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

#This python file contains all the functions used in my model creation attempts and for the wordcloud creation

def Cloud(data, Stopwords, title = None):
    wordcloud = WordCloud(
        background_color='white',
        stopwords=Stopwords,
        scale=3,
        random_state=1
    ).generate(str(data))
    
    fig = plt.figure(1, figsize=(20,20))
    plt.axis('off')
    if title:
        fig.subtitle(title, fontsize=20)
        fig.subplots_adjust(top=2.3)
    
    plt.imshow(wordcloud)
    plt.show
    
def word_counter(text_col):
    count = Counter()
    for text in text_col.values:
        for word in text.split():
            count[word] +=1
    
    return count


def remove_punc(text):
    translator = str.maketrans("", "", string.punctuation)
    
    return text.translate(translator)

def process_text(text):
    #Remove punction
    nopunc = [char for char in text if char not in string.punctuation]
    nopunc = ''.join(nopunc)
    
    #Puts words in a list
    word_list = [word for word in nopunc.split()]
    
    return word_list

def map_func(input_ids, masks, labels):
    return{'input_ids':input_ids, 'attention_mask':masks}, labels


def prep_data(text):
    tokenizer = BertTokenizer.from_pretrained('bert-base-cased')
    tokens = tokenizer.encode_plus(text, max_length=25, truncation=True, 
                                   padding='max_length', add_special_tokens=True,                                 
                                   return_tensors='tf')
    
    return {
        'input_ids': tf.cast(tokens['input_ids'],tf.float64),
        'attention_mask': tf.cast(tokens['attention_mask'],tf.float64)
    }