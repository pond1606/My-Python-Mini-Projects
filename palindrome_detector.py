"""Palindrome Detector by Phan Huynh Thien Phuc
A palindrome is a word that reads the same backward as forward.
This program can detect if a given word is a palindrome or not."""

word = input("Enter a word: ")
reverse = word[::-1]  # ":" copies the whole word, ":-1" means in reverse order
if word == reverse:
    print("It's a palindrome!")
else:
    print(f"It's not a palindrome. Here's what it looks like backward: {reverse}.")