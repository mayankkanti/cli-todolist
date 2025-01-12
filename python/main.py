import json
import os
from datetime import datetime

script_dir = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(script_dir, "todolist.json")
priority_map = {"1": "High", "2": "Medium", "3": "Low"}
status_map = {"1": "Pending", "2": "In-Progress", "3": "Completed"}

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as file:
        json.dump([], file)
        
def load_data():
    with open(DATA_FILE, "r") as file:
        return json.load(file)
    
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)
        
def read_data():
    data = load_data()
    for rec in data:
        print(rec)

def create_record(title, disc, timestamp, priority, status):
    data = load_data()
    new_record = {
        "id": len(data) + 1,
        "title": title,
        "discription": disc,
        "priority": priority,
        "status": status,
        "created_at": timestamp,
        "updated_at": timestamp
    }
    data.append(new_record)
    save_data(data)
    print(f"Record added: {new_record}")
    
def delete_record(id):
    data = load_data()
    data = [rec for rec in data if rec["id"] != id]
    if len(data) < len(data):
        save_data(data)
        print(f"Record with ID {id} deleted.")
    else:
        print(f"No record found with ID {id}.")

"""NEEDS UPDATE"""        
def update_record(record_id):
    data = load_data()
    record = next((rec for rec in data if rec["id"] == record_id), None)
    if record:
        while True:
            print()
    else:
        print(f"No record found with ID {record_id}.")
        
def main():
    while True:
        print("=======TODOLIST======")
        print(f"Current Working Directory: {os.path.dirname(os.path.abspath(__file__))}")
        print("1. Create a record.")
        print("2. Read Records.")
        print("3. Delete Records.")
        print("4. Exit Program.")
        print("=====================")
        ch = input("Enter Your Choice: ") 
        while ch not in ["1", "2", "3", "4"]:
            print("Wrong Input, Please Try Again.")
            ch = input("Enter Your Choice: ") 
        if ch == "1":
            title = input("Enter the title of note: ")
            disc = input("Enter the discription of the note: ")
            while (priority := input("Enter note priority [(1) High, (2) Medium, (3) Low]: ")) not in priority_map:
                print("Wrong Input, Enter again.")
            priority = priority_map[priority]
            while (status := input("Enter note status [(1) Pending, (2) In-Progress, (3) Completed]: ")) not in status_map:
                print("Wrong Input, Enter again.")
            status = status_map[status]
            current_datetime = datetime.now()
            timestamp = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            create_record(title, disc, timestamp, priority, status)
        elif ch == "2":
            print("Stuff for Reading Records")
        elif ch == "3":
            print("Stuff for Deleting Records")
        elif ch == "4":
            print("Exiting...")
            break
            
if __name__ == "__main__":
    main()