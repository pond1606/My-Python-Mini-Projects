"""Roll dice by Phan Huynh Thien Phuc
Simulating a dice with ASCII art."""
import random
dice = {1: """
 -----------------------
|                       |
|                       |
|                       |
|                       |
|          000          |
|          000          |
|                       |
|                       |
|                       |
|                       |
 ----------------------- 
""",
2: """
 -----------------------
|                       |
|     000               |
|     000               |
|                       |
|                       |
|                       |
|                       |
|              000      |
|              000      |
|                       |
 ----------------------- 
""",
3: """
 -----------------------
|                       |
|     000               |
|     000               |
|                       |
|          000          |
|          000          |
|                       |
|              000      |
|              000      |
|                       |
 ----------------------- 
""",
4: """
 -----------------------
|                       |
|     000      000      |
|     000      000      |
|                       |
|                       |
|                       |
|                       |
|     000      000      |
|     000      000      |
|                       |
 ----------------------- 
""",
5: """
 -----------------------
|                       |
|     000      000      |
|     000      000      |
|                       |
|          000          |
|          000          |
|                       |
|     000      000      |
|     000      000      |
|                       |
 ----------------------- 
""",
6: """
 -----------------------
|                       |
|     000      000      |
|     000      000      |
|                       |
|     000      000      |
|     000      000      |
|                       |
|     000      000      |
|     000      000      |
|                       |
 ----------------------- 
"""}
while True:
    print(dice[random.randint(1, 6)])
    a = input("Press Enter to roll again (or q to quit).")
    if a == 'q':
        print("Thanks for rolling!")
        break
