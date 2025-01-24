import sys
import os
import json
import argparse

def main():
    # take input from user through terminal 

    if os.path.isfile("tasks.json"):
        with open("tasks.json", "r") as file:
            data = json.load(file) # convert json file to python dict or list
    else: 
        data = {"todo": [], "doing": [],"done": []}
        with open("tasks.json", "w") as file:
            json.dump(data, file, indent=4)

    # creating a parser to deal with flags and categories
    parser = argparse.ArgumentParser(description="A CLI tool to manage your todo list")

    # defining arguements
    parser.add_argument(
        "category",
        choices=["todo", "doing", "done"],
        help="pick one of the categories")

    parser.add_argument(
        "-show",
        action="store_true",
        help="list tasks from category"
        )

    parser.add_argument("task", nargs="?", help="task to add (required if --show is not set)")

    args = parser.parse_args()

    if args.show == True:
        if args.category in data:
            print_list(args.category, data)
        else:
            print(f"category '{args.category}' does not exist.")
    elif args.category == "todo":
        add_task(args.task, args.category, data)
    elif args.category == "doing":
        doing_task()
    elif args.category == "done":
        done_task()
    else:
        print("error try -help")


# functions

def add_task(task, category, data):
    data[category].append(task)
    with open("tasks.json", "w") as file:
        json.dump(data, file, indent=4)
    # add debugging

def print_list(category, data):
    if category in data:
        for task in data[category]:
            print(f"* {task} \n")

def doing_task():

def done_task():


main()