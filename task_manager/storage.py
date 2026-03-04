import json
import os

BASE_DIR = os.path.dirname(__file__)
FILE_NAME = os.path.join(BASE_DIR, "tasks.json")

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)
    
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)