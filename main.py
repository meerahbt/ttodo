import sys
import os
import json

def main():
# take input from user through terminal 
    if len(sys.argv) > 1:
        task = sys.argv[1]
        add_task(task)
        print(task"Task added: {task}")

main()
# store what the user is giving 
def add_task(task):
    task = []


# return what the user is asking for 


# understanding opening files and using json with python before starting the project :s

# OPENING FILES
# standard
with open("tasks.json", "r") as file: # open in read
    data = file.read() # read file and store it as string

#same thing but convert json to python dict or list 
with open("tasks.json", "r") as file:
    data = json.load(file) # convert json file to python dict or list 

# WRITING FILES 
# writing to a file 
with open("tasks.json", "w") as file:
    file.write("this string is saved to file") # will overwrite the existing content of the file 

# writing as json 
tasks = ["list", "of", "tasks"]
with open("tasks.json", "w")
    json.dump(tasks, file)

# checking for file existence

if os.path.exists("tasks.json"):
    print("file exists")
else:
    print("file doesn't exist")
    with open("tasks.json", "w") as file:
        file.write("[]")  # write an empty list to initialize the file :s
