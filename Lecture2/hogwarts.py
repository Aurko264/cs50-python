"""students = ["Hermione", "Harry", "Ron"]"""

# One way

"""print(students[0])
print(students[1])
print(students[2])"""

# Another way

"""for student in students:
    print(student)"""

# Using length function

"""for i in range(len(students)):
    print(i + 1, students[i])"""

# Using dictionary

"""students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for student in students:
    print(student, students[student], sep=", ")"""

# Giving more information(Still using dictionary)

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russsell terrir"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")