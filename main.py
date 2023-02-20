import requests

from time import sleep

from model import Message
from model import Callback

from handler import type_handler

import Constants

def get_tasks(offset = None) -> list:
    '''retrieves a list of updates from the Telegram Bot API URL
    Creates the appropriate instance of object based on their type
    
    args:
    offset  -- used to clear mupdates that are already processed'''
    tasks = []
    try:
        url = f"https://api.telegram.org/bot{Constants.TELEGRAM_API_KEY}/getUpdates?timeout=100"
        if offset is None:
            r = requests.get(url)
        else:
            r = requests.get(f"{url}&offset={offset}")
    except:
        print("Something went wrong.")
    else:
        data = r.json()
        if len(data['result']) > 0:
            for i in data['result']:
                if "callback_query" in i:
                    callback = Callback.Callbacks(i['update_id'], i['callback_query']['message']['date'],i['callback_query']['id'], i['callback_query']['message']['chat']['id'], i['callback_query']['from']['id'], i['callback_query']['from']['username'], i['callback_query']['data'])
                    tasks.append(callback)
                elif "edited_message" in i:
                    # TODO
                    pass
                else:
                    msg = Message.Messages(i['update_id'], i['message']['date'], i['message']['message_id'], i['message']['from']['id'], i['message']['chat']['id'], i['message']['chat']['username'], i['message']['text'])
                    tasks.append(msg)
        else:
            print("No messages")

    return tasks

def process_task(tasks) -> int or None:
    '''get the type of command and call the appropriate handler to process
    
    args:
    tasks   -- possibly an array of Message model objects'''
    task_ids = []
    for task in tasks:
        if task.type == Constants.TYPE:
            x = type_handler.process(task)
            print(x)
            task_ids.append(x)
    if len(task_ids) > 0:
        return max(task_ids) + 1
    else:
        return None 


def main() -> None:
    '''constant loop to get the updates and handles them'''
    offset = None
    while True:
        if offset is None:
            latest_task = process_task(get_tasks())
            offset = latest_task
        else:
            latest_task = process_task(get_tasks(offset))
            offset = latest_task
            print("offset = " + str(latest_task))
        sleep(0.5)

if __name__ == "__main__":
    # Log responses + chat_id
    # Generate pichart
    main()