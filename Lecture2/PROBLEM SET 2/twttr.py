# PROBLEMS

# When texting or tweeting, it’s not uncommon to shorten words 
# to save time or space, as by omitting vowels, much like Twitter 
# was originally called twttr. In a file called twttr.py, 
# implement a program that prompts the user for a str of text and 
# then outputs that same text but with all vowels (A, E, I, O, 
# and U) omitted, whether inputted in uppercase or lowercase.

def main():
    text = input("Input: ")
    print("Output:", shorten(text))

def shorten(word):
    new_word = ""
    for char in word:
        if char.lower() not in ['a', 'e', 'i', 'o', 'u']:
            new_word += char
    return new_word

if __name__ == "__main__":
    main()