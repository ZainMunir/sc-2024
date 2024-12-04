import sys
from termcolor import colored
import enchant

dictionary = enchant.Dict("en_US")

# input_file = "input-1a.txt"
input_file = input(colored("Enter the input file: ", "green"))
if not input_file:
    print(colored("No input file", "red"))
    sys.exit(1)

cipher_text = ""
with open(input_file, "r") as f:
    cipher_text = f.read()
if not cipher_text:
    print(colored("No cipher text", "red"))
    sys.exit(1)

lowered_cipher_text = cipher_text.lower()
filtered_cipher_text = "".join([c.lower() for c in cipher_text if c.isalpha()])
cipher_text_len = len(filtered_cipher_text)

similarity_scores = []

for i in range(26):
    decrypted_text = ""
    for c in lowered_cipher_text:
        if c.isalpha():
            decrypted_text += chr((ord(c) - ord("a") - i) % 26 + ord("a"))
        else:
            decrypted_text += c
    words = [x for x in decrypted_text.split(" ") if x]
    num_words = len(words)
    num_english_words = sum([dictionary.check(word) for word in words])
    similarity_scores.append(num_english_words / num_words * 100)


def nth_max_index(lst, n):
    return sorted(range(len(lst)), key=lambda i: lst[i], reverse=True)[n]


potential_keys = [
    nth_max_index(similarity_scores, i) for i in range(len(similarity_scores))
]

for key in potential_keys:
    decrypted_text = ""
    for c, lc in zip(cipher_text, lowered_cipher_text):
        if lc.isalpha():
            decrypted_text += chr((ord(lc) - ord("a") - key) % 26 + ord("a"))
            if c.isupper():
                decrypted_text = decrypted_text[:-1] + decrypted_text[-1].upper()
        else:
            decrypted_text += c
    print(colored(f"Using key: {key}", "red"))
    print(decrypted_text)
    key_pressed = input(
        colored("Enter 'q' to quit or any other key to continue: ", "green")
    )
    if key_pressed == "q":
        break
