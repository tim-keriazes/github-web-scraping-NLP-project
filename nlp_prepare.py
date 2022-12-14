import re
import unicodedata
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
import pandas as pd

import nlp_acquire

def make_lower(content_list):
    cleaned_content = []
    for content in content_list:
        clean_content = {
            'repo': content['repo'].lower(),
            'language': content['language'],
            'readme_contents':content['readme_contents'].lower()
          }
        cleaned_content.append(clean_content)
    return cleaned_content

def make_no_special_chars(content_list):
    cleaned_content = []
    r_ex = r"[^a-zA-Z0-9\s]"
    for content in content_list:
        clean_content = {
            'repo': re.sub(r_ex,'', content['repo']),
            'language': content['language'],
            'readme_contents': re.sub(r_ex,'', content['readme_contents'])
        }
        cleaned_content.append(clean_content)
    return cleaned_content

def make_normal(content_list):
    cleaned_content = []
    for content in content_list:
        clean_content = {
            'repo': unicodedata.normalize('NFKD', content['repo']).encode('ascii', 'ignore').decode('utf-8', 'ignore'),
            'language': content['language'],
            'readme_contents': unicodedata.normalize('NFKD', content['readme_contents']).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        }
        cleaned_content.append(clean_content)
    return cleaned_content

def basic_clean(content_list):
    content_list = make_normal(content_list)
    content_list = make_no_special_chars(content_list)
    content_list = make_lower(content_list)
    return content_list

def tokenize(s):
    tokenizer = ToktokTokenizer()
    return tokenizer.tokenize(s)

def mass_tokenize(content_list):
    for content in content_list:
        content['clean'] = tokenize(content['readme_contents'])
    return content_list

def stem(s):
    ps = nltk.porter.PorterStemmer()
    return [ps.stem(word) for word in s]

def mass_stem(content_list):
    for content in content_list:
        content['stemmed'] = stem(content['clean'])
    return content_list

def lemmatize(s):
    wnl = nltk.stem.WordNetLemmatizer()
    return [wnl.lemmatize(word) for word in s]

def mass_lemmatize(content_list):
    for content in content_list:
        content['lemmatized'] = lemmatize(content['clean'])
    return content_list

def remove_stopwords(s, extra_words = [], exclude_words = []):
    stopwords_list = nltk.corpus.stopwords.words('english')
    stopwords_list = stopwords_list + extra_words
    return [word for word in s if word not in stopwords_list]

def mass_remove_stopwords(content_list):
    for content in content_list:
        content['clean'] = remove_stopwords(content['clean'])
    return content_list

def make_dataframe_news(text_dict):
    df = pd.DataFrame(text_dict)
    df['clean'] = df['content'].str.lower()
    df['clean'] = df['clean'].str.replace(r"[^a-zA-Z0-9\s]", "")
    df['clean'] = df['clean'].apply(lambda r : unicodedata.normalize('NFKD', r).encode('ascii', 'ignore').decode('utf-8','ignore'))
    df['clean'] = df['clean'].apply(remove_stopwords_split)
    wnl = nltk.stem.WordNetLemmatizer()
    df['lemmatized'] = df['clean'].apply(lemmatize_split)
    return df

def make_dataframe(text_dict):
    text_dict = basic_clean(text_dict)
    text_dict = mass_tokenize(text_dict)
    text_dict = mass_remove_stopwords(text_dict)
    text_dict = mass_stem(text_dict)
    text_dict = mass_lemmatize(text_dict)
    return pd.DataFrame(text_dict)