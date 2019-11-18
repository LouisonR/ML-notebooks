## TODO: import needed libraries
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from .talks import greetings_inputs, greetings_answers, goodbye_inputs, goodbye_answers, small_talks
from .preprocessing import preprocessing_func, vectorizer, tfidf, df

def get_tfidf(query):
    print(preprocessing_func(query))
    return vectorizer.transform([preprocessing_func(query)]).toarray()


## TODO: implement get_closest_sentence(query, tf_idf, vectorizer)
def get_closest_sentence(query, tfidf, vectorizer):
    query_tfidf = get_tfidf(query)
    sim = cosine_similarity(query_tfidf, tfidf)
    print(sim)
    return sim.max(), sim.argmax()


def greetings(sentence, inputs, outputs):
    for word in sentence.split():
        if word.lower() in inputs:
            return outputs[np.random.randint(len(outputs))]


## TODO: implement the function vivabot
def vivabot(query, corpus=tfidf, vectorizer=vectorizer, database=df, sim_threshold=0.1):
    print('your query is: ', query)

    greet = greetings(query, greetings_inputs, greetings_answers)

    if(greet!=None):
        answer = greet
    elif query.lower() in goodbye_inputs:
        bye = greetings(query, goodbye_inputs, goodbye_answers)
        answer = bye
    else:
        sim, closest = get_closest_sentence(query, corpus, vectorizer)
        if sim > sim_threshold:
            answer = database["data"].iloc[closest]
        else:
            answer = small_talks[np.random.randint(len(small_talks))]
    print(answer)
    return answer
