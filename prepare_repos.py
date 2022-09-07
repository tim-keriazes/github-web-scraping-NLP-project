import unicodedata
import re
import json
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
import pandas as pd

def drop_nulls(df):
    df = df.dropna()
    return df


def basic_clean(string):
    ''' Receives a string of text, processes it & then returns its normalized version.
    Normalization via standard NKFD unicode, fed into an ASII encoder & decoded back into UTF-8.
    '''
    string = string.lower()
    string = unicodedata.normalize('NFKD', string)\
    .encode('ascii', 'ignore')\
    .decode('utf-8', 'ignore')
    string = re.sub(r"[^a-z0-9'\s]", ' ', string)
    return string


def tokenize(string):
    tokenizer = nltk.tokenize.ToktokTokenizer()
    string = tokenizer.tokenize(string, return_str=True)
    return string


def lemmatize(string):
    wnl = nltk.stem.WordNetLemmatizer()
    lemmas = [wnl.lemmatize(word) for word in string.split()]
    article_lemmatized = ' '.join(lemmas)

    return article_lemmatized


def remove_stopwords(string, extra_words=None, exclude_words=None):
    
    stopword_list = stopwords.words('english')
    
    if exclude_words:
        
        stopword_list = stopword_list + exclude_words
        
    if extra_words:
        
        for word in extra_words:
            
            stopword_list.remove(word)
            
    words = string.split()
    
    filtered_words = [word for word in words if word not in stopword_list]
    
    filtered_string = ' '.join(filtered_words)
    
    return filtered_string
