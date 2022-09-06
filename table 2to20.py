num = int(input("Which table you need write it here: "))
starting_range =int(input("Write the number from where to start:"))
ending_range = int(input("Write the end of the number you need:"))
print()
print("so This is the table of",num)
for i in range(starting_range, ending_range + 1):
    print(num, 'x', i, '=', num*i)