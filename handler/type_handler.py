from csv import writer
import pandas as pd
import os
from datetime import date

import Constants
import interaction

def process(task) -> int:
    '''determines the action to be taken and sends a response to the user.
    returns the update id to be offset for the next GET query to the API link.
    
    args:
    task    - a Message model object
    '''
    print(f"Within type_handler: process (received {task.text})")
    offset = None

    if task.command_type == Constants.START:
        interaction.send_message(chat_id=task.chat_id, text=Constants.welcome_text(task.username))
    elif task.command_type == Constants.ADD_EXPENSE:
        if len(task.text.split(" ")) < 4:
            interaction.send_message(chat_id=task.chat_id, text=Constants.SAMPLE_COMMAND)
        else:
            export_to_csv(task)
            interaction.send_message(chat_id=task.chat_id, text=Constants.ACKNOWLEDGEMENT)
    elif task.command_type == Constants.NOT_A_COMMAND:
        interaction.send_message(chat_id=task.chat_id, text=Constants.ACKNOWLEDGEMENT_NOT_COMMAND)
    else:
        print("nono")
    offset = task.update_id
    print("from handler offset = " + str(offset))
    return offset

def extract_budget_details(task) -> tuple[str, str, str] or tuple[False, False, False]:
    '''extract the different details of a task
    
    args:
    task    -- a Message model object
    '''
    if isfloat(task.text.split(" ")[1]) and task.text.split(" ")[2].lower() in Constants.CATEGORIES:           
            desc = ""
            for i in task.text.split(" ")[3:]:
                desc += str(i).lower() + " "     
            return task.text.split(" ")[1], task.text.split(" ")[2], desc
    else:
        return False, False, False

def export_to_csv(task):
    '''initialises a file if does not exists, then writes the values based on the user input
    
    args:
    task    -- a Message model object
    '''
    price, category, desc = extract_budget_details(task)
    if price and category and desc:
        file_path = f"output/{task.chat_id}_expense.csv"
        data = {"date": str(date.today()), "price": str(price), "category": str(category), "desc": str(desc)}
        if not os.path.exists(file_path):
            with open(file_path, mode="w", encoding="utf-8") as f:
                f.write(",".join(["date", "price", "category", "desc"]))
                f.write("\n")
                f.close()
            df = pd.DataFrame(data, index=[0])
            df.to_csv(file_path, mode="a",encoding="utf-8", index=False, header=False)
        else:
            df = pd.DataFrame(data, index=[0])
            df.to_csv(file_path, mode="a",encoding="utf-8", index=False, header=False)
    

def isfloat(num) -> bool:
    '''checks if value is a float and returns True/False
    
    args:
    num -- to be determine if can be converted to float
    '''
    try:
        float(num)
        return True
    except ValueError:
        return False
