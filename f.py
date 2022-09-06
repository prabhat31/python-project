import difflib
 
with open('f.txt') as file_1:
    file_1_text = file_1.readlines()
 
with open('f.1txt') as file_2:
    file_2_text = file_2.readlines()
 
# Find and print the diff:
for line in difflib.unified_diff(
        file_1_text, file_2_text, fromfile='f.txt',
        tofile='f1.txt', lineterm=''):
    print(line)