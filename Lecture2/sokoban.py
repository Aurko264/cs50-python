def main():
    history = []

    while True:
        action = input("Action: ")

        if action == "Undo":
            undone = history.pop() # Will remove last element in the list.
            print(f"Undone: {undone}")
        elif action == "Restart":
            history.clear()
        elif action == "close":
            break
        else:    
            history.append(action)
            print(history)

main()