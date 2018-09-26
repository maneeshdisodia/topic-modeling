import pandas as pd
import numpy as np
import logging
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
form nltk

np.random.seed(201)
import nltk
nltk.download('wordnet')

df = pd.read_csv('abcnews-date-text.csv', error_bad_lines=False)
logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s',
    level=logging.INFO)

logging.info("work started {}".format('maneesh'))

df_text = df['headline_text']
documents = df_text
logging.info("{} of documents loaded".format(len(documents)))
print(len(documents))
print(documents[:5])


def lemmatize(text):
    """
    :param text:string
    :return: lemmatize string
    """
    return


def preprocess():
    pass
