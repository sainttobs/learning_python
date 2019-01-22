ages = [10, 15, 30, 21, 17, 19, 18, 13, 14, 18, 23]  # creating  a list of ages

adults = []  # an empty list for adults
children = []  # an empty list for children

for age in ages:  # looping through the ages list
    if age >= 18:  # if the age is 18 or above
        adults.append(age)  # add the age to the adults list
    else:
        children.append(age)  # if it is below 18 add it to the children list

print(children)  # print the children list
print(adults)