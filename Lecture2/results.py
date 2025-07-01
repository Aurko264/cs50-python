"""results = ["Mario", "Luigi"]

results.append("Princess")
results.append("Yoshi")
results.append("Koopa Troopa")
results.append("Toad")

results.append(["Bowser", "Donkey Kong Jr."]) # Working but also adding the square brackets too.
results.remove(["Bowser", "Donkey Kong Jr."]) # Removing the lists
results.extend(["Bowser", "Donkey Kong Jr."])

print(results)
"""

# More features of lists

results = ["Mario", "Luigi", "Princess", "Yoshi", "Koopa Troopa", "Toad", "Bowser", "Donkey Kong Jr"]

results.remove("Bowser") # Will remove Bowser from the list
results.insert(0, "Bowser") # Will insert Bowser in the "0" index
results.reverse() # Will reverse the list

print(results)
