import os
import glob
import json

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

def get_previous_usernames(username):
    uuid = get_uuid(username)
    if uuid is not None:
        command = f'curl -s "https://laby.net/api/user/{uuid}/get-names"'
        response = os.popen(command).read()
        if response:
            data = json.loads(response)
            if isinstance(data, list) and len(data) > 1:
                print(f"Previous usernames for {username}:")
                for name in data[:-1]:
                    print(name["name"])
                    search(name["name"])
            else:
                print("No previous usernames found.")
        else:
            print("Failed to retrieve previous usernames.")
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
            with open(file_path, "r", encoding="utf-8") as file:
                try:
                    content = file.read()
                    if query in content:
                        print(f"Found in {file_path}:")
                        print(content)
                        print()
                        break  # Stop searching other files once the exact match is found

                except Exception as e:
                    print(f"Error occurred while reading {file_path}: {e}")

while True:
    command = input("Enter a command (search, final, wak, fb): ")
    
    if command == "search":
        query = input("Enter search query: ")
        search(query)
    elif command == "final":
        username = input("Enter Minecraft username: ")
        get_previous_usernames(username)
    elif command == "wak":
        query = input("Enter Wakanim search query: ")
        wakanim_search(query)
    elif command == "fb":
        query = input("Enter France search query: ")
        france_search(query)
    elif command == "exit":
        break
    else:
        print("Invalid command. Please try again.")

print("Script terminated.")