"""Ceasar Cipher by Phan Huynh Thien Phuc
A simple and famous encryption technique. Each letter in the plaintext is replaced by a letter
some fixed number of positions down the alphabet (also called: key). For example, with key 3,
A would be D, B would be E. This program has a brute-force mode which will try all the possible keys.
Idea from the book "Invent your own computer games with Python" by Al Sweigart.
I rewrote it with my style, I found my style easier to read and understand.
This version uses Vietnamese alphabet, which doesn't have f, w or z."""

SYMBOLS = 'aáàảãạăắằẳẵặâấầẩẫậbcdđeéèẻẽẹêếềểễệghiíìỉĩịjklmnoóòỏõọôốồổỗộơớờởỡợpqrstuúùủũụưứừửữựvxy'
max_key_size = len(SYMBOLS)

def translate_message(mode, message, key):
    """Translate the message with the given mode and key."""
    if mode in ['d', 'decrypt']:
        key = -key
    translated_message = ''
    for symbol in message:
        symbol_index = SYMBOLS.find(symbol)
        if symbol_index == -1:  # Not found this symbol
            translated_message += symbol  # Just add this symbol normally
        else:
            symbol_index += key  # New index

            if symbol_index >= len(SYMBOLS):
                symbol_index -= len(SYMBOLS)
            elif symbol_index < 0:
                symbol_index += len(SYMBOLS)

            translated_message += SYMBOLS[symbol_index]  # Add the new symbol to the string
    return translated_message

# Ask for the mode
mode = ''
while mode not in ['b', 'brute', 'd', 'decrypt', 'e', 'encrypt']:
    mode = input("Do you want to (e)ncrypt, (d)ecrypt or (b)rute-force a message? ")

# Ask for the message
message = input("Enter your message: ")

if mode in ['d', 'decrypt', 'e', 'encrypt']:  # Encrypt/decrypt mode
    # Ask for the key
    key = ''
    while key not in range(1, max_key_size + 1):
        key = input(f"Enter the key (1-{max_key_size}): ")
        try:
            key = int(key)
        except ValueError:
            print("You must enter a NUMBER!")

    # Translate the message
    new_message = translate_message(mode, message, key)
    print(f"Your translated message: {new_message}")
else:  # Brute-force mode
    for i in range(1, max_key_size + 1):
        print(f"Key: {i}. Message: {translate_message('d', message, i)}")



