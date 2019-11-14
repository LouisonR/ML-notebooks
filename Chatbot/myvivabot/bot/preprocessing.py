import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.corpus import wordnet

def get_wordnet_pos(pos_tag):
    output = np.asarray(pos_tag)
    for i in range(len(pos_tag)):
        if pos_tag[i][1].startswith('J'):
            output[i][1] = wordnet.ADJ
        elif pos_tag[i][1].startswith('V'):
            output[i][1] = wordnet.VERB
        elif pos_tag[i][1].startswith('R'):
            output[i][1] = wordnet.ADV
        else:
            output[i][1] = wordnet.NOUN
    return output


lemmatizer = WordNetLemmatizer()
stop_words = stopwords.words("english")

def preprocessing_func(article):
    tokens = word_tokenize(article)
    tokens = [t.lower() for t in tokens if t.isalpha()]
    tokens = [t for t in tokens if t not in stop_words]
    tokens_postag = get_wordnet_pos(pos_tag(tokens))
    tokens_clean = [lemmatizer.lemmatize(t, postag) for t, postag in tokens_postag]
    return tokens


## TODO: load chatbot_database.txt
df = pd.read_csv('data/chatbot_database.txt', sep='\n', header=None, names=["data"])
# Text preprocessing
df["tokens"] = df["data"].apply(lambda x: preprocessing_func(x))
# Instantiate the TF-IDF vectorizer
vectorizer = TfidfVectorizer(analyzer=lambda x: x)
# Compute the TF-IDF
tfidf = vectorizer.fit_transform(df['tokens']).toarray()
