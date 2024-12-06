import sys
from termcolor import colored

# http://en.wikipedia.org/wiki/Letter_frequency
english_frequency = {
    "a": 8.2,
    "b": 1.5,
    "c": 2.8,
    "d": 4.3,
    "e": 12.7,
    "f": 2.2,
    "g": 2.0,
    "h": 6.1,
    "i": 7.0,
    "j": 0.15,
    "k": 0.77,
    "l": 4.0,
    "m": 2.4,
    "n": 6.7,
    "o": 7.5,
    "p": 1.9,
    "q": 0.095,
    "r": 6.0,
    "s": 6.3,
    "t": 9.1,
    "u": 2.8,
    "v": 0.98,
    "w": 2.4,
    "x": 0.15,
    "y": 2.0,
    "z": 0.074,
}

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
letter_counts = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
    "g": 0,
    "h": 0,
    "i": 0,
    "j": 0,
    "k": 0,
    "l": 0,
    "m": 0,
    "n": 0,
    "o": 0,
    "p": 0,
    "q": 0,
    "r": 0,
    "s": 0,
    "t": 0,
    "u": 0,
    "v": 0,
    "w": 0,
    "x": 0,
    "y": 0,
    "z": 0,
}
for c in filtered_cipher_text:
    letter_counts[c] += 1

letter_frequencies = {k: v / cipher_text_len * 100 for k, v in letter_counts.items()}

english_numbers = list(english_frequency.values())
cipher_numbers = list(letter_frequencies.values())

similarity_scores = []

for i in range(len(english_numbers)):
    cipher_numbers = cipher_numbers[-1:] + cipher_numbers[:-1]
    similarity_scores.append(
        sum(
            [
                abs(english_numbers[j] - cipher_numbers[j])
                for j in range(len(english_numbers))
            ]
        )
    )


def nth_min_index(lst, n):
    return sorted(range(len(lst)), key=lambda i: lst[i])[n]


potential_keys = [
    nth_min_index(similarity_scores, i) for i in range(len(similarity_scores))
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
