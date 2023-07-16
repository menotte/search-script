import os
import glob
import json
import re
from colorama import Fore, Style

def search(query):
    command = f"findstr /S /I /C:'{query}' database/*"
    os.system(command)

def get_uuid(username):
    command = f'curl -s "https://laby.net/api/search/names/{username}"'
    response = os.popen(command).read()
    if response:
        data = json.loads(response)
        if "results" in data and len(data["results"]) > 0:
            return data["results"][0]["uuid"]
    return None

def get_usernames(uuid):
    command = f'curl -s "https://laby.net/api/user/{uuid}/get-names"'
    response = os.popen(command).read()
    if response:
        data = json.loads(response)
        if isinstance(data, list) and len(data) > 0:
            return [name["name"] for name in data]
    return []

def get_previous_usernames(username):
    uuid = get_uuid(username)
    if uuid is not None:
        usernames = get_usernames(uuid)
        if len(usernames) > 0:
            print(f"Usernames for {username}:")
            for name in usernames:
                print(f"{Fore.RED}Username:{Style.RESET_ALL} {name}")
                search(name)
        else:
            print("No usernames found for the user.")
    else:
        print("No UUID found for the username.")

def wakanim_search(query):
    command = f"findstr /S /I /C:'{query}' wakanim/*"
    os.system(command)

def france_search(query):
    extensions = (".txt", ".json", ".sql")
    print(f"Searching in France directory for '{query}':")
    file_paths = glob.glob("france/**", recursive=True)
    for file_path in file_paths:
        if os.path.isfile(file_path) and file_path.lower().endswith(extensions):
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                    lines = content.splitlines()
                    for line in lines:
                        if query.lower() in line.lower():
                            line = line.replace(query, f"{Fore.RED}{query}{Style.RESET_ALL}")
                            print(f"Found in {file_path}:")
                            print(f"Username: {line}")
                            print()
            except Exception as e:
                print(f"Error occurred while reading {file_path}: {e}")

while True:
    print(f"{Fore.GREEN}Enter a command:{Style.RESET_ALL}\n")
    print(f"[{Fore.GREEN}1{Style.RESET_ALL}] search")
    print(f"[{Fore.GREEN}2{Style.RESET_ALL}] final")
    print(f"[{Fore.GREEN}3{Style.RESET_ALL}] wak")
    print(f"[{Fore.GREEN}4{Style.RESET_ALL}] fb")
    print(f"[{Fore.GREEN}5{Style.RESET_ALL}] exit")

    command = input("\nEnter the command number: ")

    if command == "1":
        query = input("Enter search query: ")
        search(query)
    elif command == "2":
        username = input("Enter Minecraft username: ")
        get_previous_usernames(username)
    elif command == "3":
        query = input("Enter Wakanim search query: ")
        wakanim_search(query)
    elif command == "4":
        query = input("Enter France search query: ")
        france_search(query)
    elif command == "5":
        break
    else:
        print("Invalid command number. Please try again.")

print("Script terminated.")
