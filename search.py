import os
import json
from colorama import Fore, Style
import subprocess

def search(query, directory):
    command = ["rg", "-i", query, directory]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()

    if stdout:
        print(stdout.decode("utf-8"))
    elif stderr:
        print(stderr.decode("utf-8"))
    else:
        print("No results found.")

def get_previous_usernames(username):
    command = f'curl -s "https://laby.net/api/search/names/{username}"'
    response = os.popen(command).read()
    if response:
        data = json.loads(response)
        if "results" in data and len(data["results"]) > 0:
            uuid = data["results"][0]["uuid"]
            command = f'curl -s "https://laby.net/api/user/{uuid}/get-names"'
            response = os.popen(command).read()
            if response:
                usernames = [name["name"] for name in json.loads(response)]
                if len(usernames) > 0:
                    print(f"{Fore.RED}Usernames for {username}:{Style.RESET_ALL}")
                    for name in usernames:
                        print(f"{Fore.RED}Username:{Style.RESET_ALL} {name}")
                        search(name, "database/")
                else:
                    print("No usernames found for the user.")
            else:
                print("Failed to retrieve previous usernames.")
        else:
            print("No UUID found for the username.")
    else:
        print("Failed to retrieve UUID for the username.")

def wakanim_search(query):
    search(query, "wakanim/")

def france_search(query):
    search(query, "france/")

title = """
   _____                     _     
  / ____|                   | |    
 | (___   ___  __ _ _ __ ___| |__  
  \___ \ / _ \/ _` | '__/ __| '_ \ 
  ____) |  __/ (_| | | | (__| | | |
 |_____/ \___|\__,_|_|  \___|_| |_|
                                   
                                   
"""

while True:
    print(f"{Fore.GREEN}{title}{Style.RESET_ALL}\n")
    print(f"[{Fore.GREEN}1{Style.RESET_ALL}] search")
    print(f"[{Fore.GREEN}2{Style.RESET_ALL}] final")
    print(f"[{Fore.GREEN}3{Style.RESET_ALL}] wakanim")
    print(f"[{Fore.GREEN}4{Style.RESET_ALL}] facebook")
    print(f"[{Fore.GREEN}5{Style.RESET_ALL}] exit")

    command = input(f"\n{Fore.GREEN}Enter the command number:{Style.RESET_ALL} ")

    if command == "1":
        query = input(f"{Fore.RED}Enter search query:{Style.RESET_ALL} ")
        search(query, "database/")
    elif command == "2":
        username = input(f"{Fore.RED}Enter Minecraft username:{Style.RESET_ALL} ")
        get_previous_usernames(username)
    elif command == "3":
        query = input(f"{Fore.RED}Enter Wakanim search query:{Style.RESET_ALL} ")
        wakanim_search(query)
    elif command == "4":
        query = input(f"{Fore.RED}Enter Facebook search query:{Style.RESET_ALL} ")
        france_search(query)
    elif command == "5":
        break
    else:
        print("Invalid command number. Please try again.")

print("Script terminated.")
