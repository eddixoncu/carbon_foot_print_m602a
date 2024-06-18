import os
path = "C:\\Files\\Code\\repo\\carbon_foot_print_m602a_py\\files\\file.txt"
"""
print (f'processing file {path}')
f = open (path, 'r')
#print (f.read())
print (f.read(4))

f.close()
"""

file1 = open(path, "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London\n"]
file1.writelines(L)
file1.close()

with open(path) as file :
    line = file .readline()
    print( line)

with open(path) as file :
    lines = file .readlines()
    print(f'the contains {len(lines)} lines')

    for line in lines:
        print(line)

with open(path, 'a') as file :
    data = input ('enter the new data: ')
    file.write(data)


with open(path, 'r') as text :

    d = dict()

    # Loop through each line of the file
    for line in text:
        # Remove the leading spaces and newline character
        line = line.strip()

        # Convert the characters in line to
        # lowercase to avoid case mismatch
        line = line.lower()

        # Split the line into words
        words = line.split(" ")

        # Iterate over each word in line
        for word in words:
            # Check if the word is already in dictionary
            if word in d:
                # Increment count of word by 1
                d[word] = d[word] + 1
            else:
                # Add the word to dictionary with count 1
                d[word] = 1

    # Print the contents of dictionary
    for key in list(d.keys()):
        print(key, ":", d[key])


f = open (path, 'r')
info = f.read()
f.close()

info = info .replace("This", "That")

with open(path, 'w') as file :
    file.write(info)

os.remove(path)