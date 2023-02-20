import Constants

import requests

# from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def send_message(chat_id, text):
    '''Creates a POST request to the Telegram API Bot URL
    
    args:
    chat_id -- determines which chat for the message to be sent to
    text    -- the message to be sent to the chat

    '''
    
    data = {
        "chat_id" : chat_id,
        "text" : text
    }
    try:
        requests.post(f"https://api.telegram.org/bot{Constants.TELEGRAM_API_KEY}/sendMessage", data = data)
    except:
        # Log an error when replying
        print("Something went wrong...")
    else:
        # Log the reply
        print("Replied")


# def send_message(chat_id, text):
#     keyboard = [[InlineKeyboardButton("add an expense", callback_data=Constants.ADD_EXPENSE)],
#             [InlineKeyboardButton("wip", callback_data='wip'),
#              InlineKeyboardButton("wip", callback_data='wip')]]

#     reply_markup = InlineKeyboardMarkup(keyboard) 

#     data = {
#         "chat_id" : chat_id,
#         "text" : text,
#         "reply_markup": json.dumps(reply_markup.to_dict())
#     }

#     r = requests.post(f"https://api.telegram.org/bot{Constants.TELEGRAM_API_KEY}/sendMessage", 
#             data = data)
#     print(r.json())