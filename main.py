import sys
import os
import json
import argparse

def main():

    # creating json file

    if os.path.isfile("tasks.json"):
        with open("tasks.json", "r") as file:
            data = json.load(file) # convert json file to python dict or list
    else: 
        data = {"todo": [], "doing": [],"done": []}
        with open("tasks.json", "w") as file:
            json.dump(data, file, indent=4)

    # handling parser and arguments
    parser = argparse.ArgumentParser(description="A CLI tool to manage your todo list")

    parser.add_argument(
        "category",
        nargs="?",
        choices=["todo", "doing", "done"],
        help="pick one of the categories")

    parser.add_argument(
        "-s", "--show",
        action="store_true",
        help="list tasks from category"
        )
    
    parser.add_argument(
        "-r", "--remove",
        action="store_true",
        help="remove tasks from category"
    )

    parser.add_argument(
        "-a", "--all",
        action="store_true",
        help="goes through all categories"
    )

    parser.add_argument("task", nargs="?", help="task to add (required if --show is not set)")

    args = parser.parse_args()

    #running the program/menu

    if not (args.show and args.all) and args.task is None:
        print("Error: 'task' is required unless you are using --show with --all.")
        sys.exit(1)

    if args.show == True and args.remove == False:
        if args.all:
            for category in data:
                print_list(category, data)
                print("--------------")
        elif args.category:
            if args.category in data:
                print_list(args.category, data)
        else:
            print(f"category '{args.category}' does not exist.")
    elif args.category == "todo" and args.remove == False:
        add_task(args.task, args.category, data)
        print_list(args.category, data)
    elif args.category == "doing" and args.remove == False:
        if args.task not in args.category:
            add_task(args.task, args.category, data)
        else:
            move_task("todo", "doing", args.task, data)
        print_list(args.category, data)
    elif args.category == "done" and args.remove == False:
        move_task("doing", "done", args.task, data)
        print_list(args.category, data)
    elif args.remove:
        remove_task(args.task, args.category, data)
        print_list(args.category, data)
    else:
        print("error try -help")


# functions

def add_task(task, category, data):
    if task not in data[category]:
        data[category].append(task)
        with open("tasks.json", "w") as file:
            json.dump(data, file, indent=4)
    else:
        print("task already in category.")

def print_list(category, data):
    if category in data:
        for task in data[category]:
            # print(f"{data[category].index(task) + 1}. {category.upper()} {task}")
            print(f"{category.upper()} {task}")

def remove_task(task, category, data):
    if task in data[category]:
        data[category].remove(task)
        with open("tasks.json", "w") as file:
            json.dump(data, file, indent=4)
    else:
        print("task is not in category.")

def move_task(from_category, to_category, task, data):
    if task not in data[from_category]:
        print(f"task is not in {from_category}.")
    else:
        add_task(task, to_category, data)
        remove_task(task, from_category, data)


# features to add:
# add more than one task at a time 
# manage from index of task?
# remove all 


main()