import requests
from bot.core import vivabot


def verify_webhook(req, VERIFY_TOKEN):
    """Handles the initial authentication between Facebook and your app"""
    if req.args.get("hub.verify_token") == VERIFY_TOKEN:
        print("connection OK")
        return req.args.get("hub.challenge")
    else:
        return "incorrect"


def is_user_message(message):
    """Check if the message is a message from the user"""
    return (message.get('message') and
            message['message'].get('text') and
            not message['message'].get("is_echo"))


def respond(sender_id, message, FB_API_URL, PAGE_ACCESS_TOKEN):
    """Formulate a response to the user and pass it on to a function that sends it."""
    response = vivabot(message)
    print("respond: ", response)
    if sender_id == "admin":
        return response
    else:
        send_message(sender_id, response, FB_API_URL, PAGE_ACCESS_TOKEN)


def send_message(recipient_id, text, FB_API_URL, PAGE_ACCESS_TOKEN):
    """Send a response to Facebook"""

    payload = { 'message': {'text': text},
                'recipient': {'id': recipient_id},
                'notification_type': 'regular'}

    auth = {'access_token': PAGE_ACCESS_TOKEN}

    response = requests.post(FB_API_URL, params=auth, json=payload)

    return response.json()
