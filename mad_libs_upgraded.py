"""Mad Libs upgraded version by Phan Huynh Thien Phuc
Enter some adjective, noun, verb... and the program will generate a sentence for you.
In this upgraded version, I added lots of sample sentences and stored it in a list.
The program will pick a random sentence and print it out with the words you entered.
You can add more sentences! Why not? Let your imagination fly!"""

import random

while True:
    adj = input("Adjective: ")
    noun = input("Noun: ")
    adv = input("Adverb: ")
    verb = input("Verb: ")
    sample_sentences = [
f"""I saw a(n) {adj} {noun}. I quickly ran to it to {verb} it.
It was {adv} exhausting but I finally managed to {verb} it.""",

f"""You are a bloodthirsty {noun}, waving your {adj} sword in the air to scare everybody.
A sexy lady is going by and the sword hits her. She screams at you, telling you to watch out
because she will {verb} you {adv}.""",

f"""My uncle has a(n) {adj} {noun}. It's very annoying but he promises to {verb} it.
Everybody finds it irritating but I think it's {adv} peaceful."""]
    print(random.choice(sample_sentences))
    play_again = input("Want to play again? (yes/no)")
    if play_again == "no":
        print("Thanks for playing!")
        break
