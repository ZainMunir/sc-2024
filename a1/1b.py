import sys
from termcolor import colored

input_file = "input-1a.txt"
# input_file = input(colored("Enter the input file: ", "green"))
if not input_file:
    print(colored("No input file", "red"))
    sys.exit(1)

cipher_text = ""
with open(input_file, "r") as f:
    cipher_text = f.read()
if not cipher_text:
    print(colored("No cipher text", "red"))
    sys.exit(1)
