WORDS = {"PAIR": 4, "HAIR": 4, "CHAIR": 5, "GRAPHIC": 7}

def main():
    print("Welcome to Spelling Bee1!")
    print("Your letters are: A I P C R H G")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left!")
        guess = input("Guess a word: ")

        if guess == "GRAPHIC":
            WORDS.clear()
            print("You have won!")
        if guess in WORDS.keys():
            points = WORDS.pop(guess) # will give value of the key and then remove it.
            print(f"Good job! You scored {points} points.")

            print("That's the game")

main() 