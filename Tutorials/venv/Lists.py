lucky_numbers = [4,8,15,23,16,42]
friends = ["Kevin", "Karen", "Jim", "Oscars", "Toby", "Toby"]

print(friends)
print(friends[2])
print(friends[2:])

friends.extend(lucky_numbers)
friends.append("Creed")
friends.insert(1, "Kelly")
friends.remove("Jim")

print(friends.index("Toby"))
print(friends.count("Toby"))

friends1 = ["Kevin", "Karen", "Jim", "Oscars", "Toby", "Toby"]
friends1.sort()
print(friends1)

lucky_numbers1 = [4,5,35,23,76,42]
lucky_numbers1.reverse()
print(lucky_numbers1)

friends1 = friends.copy()
print(friends1)



