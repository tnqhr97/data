# 1
subjects = ["physics","calculus","poetry","history"]
# 2
grades = ["98","97","85","88"]
# 3
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85],["history", 88]]
# 4
print(gradebook)
# 5
gradebook.append(["computer_science", 100])
# 6
gradebook.append(["visual arts", 93])
# 7
gradebook[-1].remove(93)
gradebook[-1].append(98)
# 8
gradebook[2].remove(85)
# 9
gradebook[2].append("Pass")
# 10
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]
full_gradebook = [last_semester_gradebook + gradebook]

print(full_gradebook)