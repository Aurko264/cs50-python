def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi"]

    # using for loop
    
    """for i in range(len(names)):
        print(write_letter(names[i], "Princess Peach"))"""

    # Another way to write it

    for name in names:
        print(write_letter(name, "Princess Peach"))

def write_letter(receiver,sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    Dear {receiver}

    You are cordinally invited to a ball at 
    Peach's Castel this evening, 7:00 PM.

    Sincerely
    {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    """

main()