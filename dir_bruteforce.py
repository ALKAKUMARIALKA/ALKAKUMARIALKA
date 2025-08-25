import requests

url = input("Enter target URL (with http/https): ").rstrip("/")
wordlist = input("Enter wordlist file path: ")

with open(wordlist, "r") as f:
    for line in f:
        word = line.strip()
        test_url = f"{url}/{word}"
        r = requests.get(test_url)
        if r.status_code == 200:
            print(f"[FOUND] {test_url}")
