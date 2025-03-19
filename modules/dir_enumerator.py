import requests

def dir_enumerator(url):
    wordlist = ["admin", "login", "uploads", "images"]
    print(f"\n[+] Enumerating directories on {url}")
    for word in wordlist:
        full_url = f"{url}/{word}"
        response = requests.get(full_url)
        if response.status_code == 200:
            print(f"[FOUND] {full_url}")
