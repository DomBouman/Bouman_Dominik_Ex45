import random

def Death():

    pain = [
    "You have died. Better luck next time!",
    "What are you doing man? Try again!",
    "Better luck next time!"
    ]

    print(random.choice(pain))
    exit(1)
