
"""Project Description
The goal of this project is to create a Python script that reads data stored in a JSON file, processes the information,
and identifies individuals who are minors (under 18 years old).

The program should use the json, os, os.path, and datetime modules to properly handle file operations and date calculations
"""
import os
import json
from datetime import datetime

# 1 Open and read file

data_file = "json_program1.json"

try:
    #create full file path
    file_path = os.path.join(os.getcwd(), data_file)

    with open(file_path, "r", encoding="utf-8") as file:
        people = json.load(file)

    print("Data loaded successfully.")

# 2 Display the loaded data (to check)
    #print(people)
    #print(type(people))

# 3 Calculating age and displaying minors only

# Current date
    today=datetime.today()

# Loop through all persons
    for person in people:
    # Convert birthdate string into a datetime object
        birthdate = datetime.strptime(person["birth_date"], "%Y-%m-%d")

    # Calculate exact age
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    # Display minors only
        if age < 18:
            print("Name: ", person["name"] + "\n" + "Birthdate: ", person["birth_date"] + "\n" + "Gender: ", person["gender"] + "\n" + "Age", age, "\n")


except FileNotFoundError:
    print("Error: The file was not found")

except json.JSONDecodeError:
    print("Error: Invalid JSON format")

except Exception as e:
    print ("An unexpected error ourred:", e)






