# QUESTION

# In a file called playback.py, implement a program in Python that prompts the user for input and then outputs that 
# same input, replacing each space with ... (i.e., three periods).

mess = input("Enter your message")
ret = mess.replace(" ", "...")
print(ret)