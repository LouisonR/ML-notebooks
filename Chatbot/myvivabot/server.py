from flask import Flask, request
from server_aux import verify_webhook, is_user_message, respond
from bot.core import vivabot, greetings_inputs, greetings_answers, tf_idf, vectorizer, df

Callback_URL = "https://vivabot.serveo.net/webhook"

FB_API_URL = 'https://graph.facebook.com/v2.6/me/messages'
VERIFY_TOKEN = 'vd_bot'# <paste your verify token here>
#PAGE_ACCESS_TOKEN = "EAAG82LfAveIBAJZASKwq2oJ0ZA8ndbOf2o6FpAkxZAvGmqi0PERk1LIITBiYmU8c9sbv4c3Y3gm2ZAUEAGbm9J6p77pb99DvvWq2gn3zyo1ILjUJJpWFrwTjjUfbodR6ZCFoZC1UU5tfYM2ZATt162DxS91LOq26tiwJU9kZCsy4WgZDZD"
PAGE_ACCESS_TOKEN = "EAAGX4WEYd2oBADFfNdH5zZBky7aYIKB6YV8oz4eYQn57QBcZCoWZBs6YcWZBrn48dWTr7JzcYHEV4iV4XVkwZBZAE2jZBfjRYXVb0MPlnD0ISTEXP410j0gZCAa8rhLldCtlXDJKcFZBreJ5NbJWGkg8fEYxihTwS1lj03evdVGqZA1QZDZD"
app = Flask(__name__)


# route to listen and respond to Messenger
#https://vivabot.serveo.net/webhook
@app.route("/webhook", methods=['GET','POST'])
def listen():
    print("entering listen function")
    """This is the main function flask uses to listen at the `/webhook` endpoint"""
    if request.method == 'GET':
        print("GET method")
        return verify_webhook(request, VERIFY_TOKEN)

    if request.method == 'POST':
        print("POST method")
        payload = request.json
        event = payload['entry'][0]['messaging']
        for x in event:
            if is_user_message(x):
                text = x['message']['text']
                sender_id = x['sender']['id']
                respond(sender_id, text, FB_API_URL, PAGE_ACCESS_TOKEN)

        return "ok"



# route to test that your flask app is running
#https://vivabot.serveo.net/test
@app.route("/test")
def test():
    return "Your messenger app is running"


# route to check the feedback of a specific query:
#https://vivabot.serveo.net/test_query?query=qu'est ce qu'un chatbot
@app.route("/test_query")
def test_query():
    query = request.args.get('query', default = "", type = str)
    return vivabot(query, greetings_inputs, greetings_answers, tf_idf, vectorizer, df)
