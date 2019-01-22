ages = [10, 15, 30, 21, 17, 19, 18, 13, 14, 18, 23]  # creating  a list of ages

adult = []  # an empty list for adults
children = []  # an empty list for children

for age in ages:
    if age >= 18:
        adult.append(age)
    else:
        children.append(age)

print(children)
print(adult)