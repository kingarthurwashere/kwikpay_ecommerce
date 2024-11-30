import json


def process_message(data):
    # Parse incoming data
    message = data.get('messages', [])[0]
    text = message.get('text', {}).get('body', '')

    # Example response logic
    if 'hello' in text.lower():
        return "Hi! How can I assist you today?"
    elif 'buy' in text.lower():
        return "Sure, please share the product name or ID."
    else:
        return "I'm sorry, I didn't understand that."
