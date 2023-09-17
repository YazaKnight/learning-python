age = 10
counter = 0
if age % 2 == 0:
    counter = 2
elif age % 2 != 0:
    counter = 1

while counter <= age:
    print(counter)
    counter = counter + 2