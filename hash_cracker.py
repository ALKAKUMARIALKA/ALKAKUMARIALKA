import hashlib

def crack_hash(hash_to_crack, wordlist):
    with open(wordlist, 'r', errors='ignore') as f:
        for word in f:
            word = word.strip()
            if hashlib.md5(word.encode()).hexdigest() == hash_to_crack:
                print(f"[+] Hash cracked: {word}")
                return
    print("[-] Password not found in wordlist")

if __name__ == "__main__":
    hash_input = input("Enter MD5 hash: ")
    wordlist = input("Enter path to wordlist: ")
    crack_hash(hash_input, wordlist)
