# QUESTION

# In a file called coke.py, implement a program that prompts the 
# user to insert a coin, one at a time, each time informing the 
# user of the amount due. Once the user has inputted at least 50 
# cents, output how many cents in change the user is owed. Assume 
# that the user will only input integers, and ignore any integer 
# that isn’t an accepted denomination.

def main():
    amount_due = 50

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin_input = input("Insert Coin: ")

        if coin_input.isdigit():
            coin = int(coin_input)
            if coin == 25:
                amount_due = amount_due - 25
            elif coin == 10:
                amount_due = amount_due - 10
            elif coin == 5:
                amount_due = amount_due - 5

    change_owed = 0 - amount_due
    print(f"Change Owed: {change_owed}")

if __name__ == "__main__":
    main()
