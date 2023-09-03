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

def get_previous_usernames(username, directory):
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
                        search(name, directory)
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

def facebook_search(query):
    search(query, "facebook/")

def fivem_search(query):
    search(query, "fivem/")

def linkedin_search(query):
    search(query, "linkedin/")

def twitter_search(query):
    search(query, "twitter/")

def deezer_search(query):
    search(query, "deezer/")

def twitch_search(query):
    search(query, "twitch/")

def canva_search(query):
    search(query, "canva/")

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
    print(f"[{Fore.GREEN}1{Style.RESET_ALL}] minecraft")
    print(f"[{Fore.GREEN}2{Style.RESET_ALL}] final")
    print(f"[{Fore.GREEN}3{Style.RESET_ALL}] wakanim")
    print(f"[{Fore.GREEN}4{Style.RESET_ALL}] fivem")
    print(f"[{Fore.GREEN}5{Style.RESET_ALL}] linkedin")
    print(f"[{Fore.GREEN}6{Style.RESET_ALL}] twitter")
    print(f"[{Fore.GREEN}7{Style.RESET_ALL}] deezer")
    print(f"[{Fore.GREEN}8{Style.RESET_ALL}] facebook")
    print(f"[{Fore.GREEN}9{Style.RESET_ALL}] twitch")
    print(f"[{Fore.GREEN}10{Style.RESET_ALL}] canva")
    print(f"[{Fore.GREEN}11{Style.RESET_ALL}] exit")

    command = input(f"\n{Fore.GREEN}Enter the command number:{Style.RESET_ALL} ")

    if command == "1":
        query = input(f"{Fore.RED}Enter Minecraft username:{Style.RESET_ALL} ")
        search(query, "minecraft/")
    elif command == "2":
        username = input(f"{Fore.RED}Enter Minecraft username:{Style.RESET_ALL} ")
        directory = input(f"{Fore.RED}Enter directory to search in (e.g., 'database/'): {Style.RESET_ALL}")
        get_previous_usernames(username, directory)
    elif command == "3":
        query = input(f"{Fore.RED}Enter Wakanim search query:{Style.RESET_ALL} ")
        wakanim_search(query)
    elif command == "4":
        query = input(f"{Fore.RED}Enter FiveM search query:{Style.RESET_ALL} ")
        fivem_search(query)
    elif command == "5":
        query = input(f"{Fore.RED}Enter LinkedIn search query:{Style.RESET_ALL} ")
        linkedin_search(query)
    elif command == "6":
        query = input(f"{Fore.RED}Enter Twitter search query:{Style.RESET_ALL} ")
        twitter_search(query)
    elif command == "7":
        query = input(f"{Fore.RED}Enter Deezer search query:{Style.RESET_ALL} ")
        deezer_search(query)
    elif command == "8":
        query = input(f"{Fore.RED}Enter Facebook search query:{Style.RESET_ALL} ")
        facebook_search(query)
    elif command == "9":
        query = input(f"{Fore.RED}Enter Twitch search query:{Style.RESET_ALL} ")
        twitch_search(query)
    elif command == "10":
        query = input(f"{Fore.RED}Enter Canva search query:{Style.RESET_ALL} ")
        canva_search(query)
    elif command == "11":
        break
    else:
        print("Invalid command number. Please try again.")

print("Script terminated.")
