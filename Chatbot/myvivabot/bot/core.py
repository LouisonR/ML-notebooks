## TODO: import needed libraries
import nltk
import numpy as np
import pandas as pd
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


## TODO: load chatbot_database.txt
df = pd.read_csv('data/chatbot_database.txt', sep='\n', header=None)



## TODO: preprocess and compute the TF-IDF of this database
# Tokenize
df['tokens'] = df[0].apply(lambda df: nltk.word_tokenize(df))
# Remove punctuation
df['alpha'] = df['tokens'].apply(lambda x: [item for item in x if item.isalpha()])
# Remove stop words
stop = stopwords.words('english')
df['stop'] = df['alpha'].apply(lambda x: [item for item in x if item not in stop])
# Stem
#stemmer = PorterStemmer()
#df['stemmed'] = df['stop'].apply(lambda x: [stemmer.stem(item) for item in x])
# Instantiate the TF-IDF vectorizer
vectorizer = TfidfVectorizer(lowercase=False, analyzer=lambda x: x)
# Compute the TF-IDF
tf_idf = vectorizer.fit_transform(df['stop']).toarray()



## TODO: implement get_closest_sentence(query, tf_idf, vectorizer)
def get_closest_sentence(query, tf_idf, vectorizer):
    query_df = pd.Series(query)
    query_df['tokens'] = query_df.apply(lambda df: nltk.word_tokenize(df))

    # Remove punctuation
    query_df['alpha'] = query_df['tokens'].apply(lambda x: [item for item in x if item.isalpha()])

    # Remove stop words
    query_df['stop'] = query_df['alpha'].apply(lambda x: [item for item in x if item not in stop])


    query_tf_idf = vectorizer.transform(query_df['stop'])

    sim = cosine_similarity(query_tf_idf, tf_idf)

    return sim.argmax()



## TODO: Implement the function greetings
greetings_inputs = ['hello', 'hi', 'good morning', 'hey']
greetings_answers = ['Hey there, I am Vivabot, how can I help you?', 'Hello, my name is Vivabot, nice to meet you.',
                     'Vivabot at your service, sir.', 'Hi Master, I am Vivabot.']

def greetings(sentence, greetings_inputs, greetings_outputs):
    for word in sentence.split():
        if word.lower() in greetings_inputs:
            return greetings_outputs[np.random.randint(len(greetings_outputs))]



## TODO: implement the function vivabot
def vivabot(query, greetings_inputs, greetings_outputs, tf_idf, vectorizer, database):
    print('your query is: ', query)

    greet = greetings(query, greetings_inputs, greetings_outputs)

    if(greet!=None):
        answer = "Vivabot: "+greet
    elif query.lower()=="bye":
        answer = "Bye! Have a wonderful day!"
    else:
        closest = get_closest_sentence(query, tf_idf, vectorizer)
        answer = database[0].iloc[closest]
    print(answer)
    return answer


##vivabot test
#query = "qu'est ce qu'un chatbot ?"
#vivabot(query, greetings_inputs, greetings_answers, tf_idf, vectorizer, df)
