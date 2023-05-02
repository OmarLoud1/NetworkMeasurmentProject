

with open('1.txt', 'r') as file1:
    file1_contents = set(file1.readlines())

# read in the contents of the second file and store each line in a set
with open('IPS/fed2', 'r') as file2:
    file2_contents = set(file2.readlines())

# use set intersection to find lines that are present in both sets
common_lines = file1_contents.intersection(file2_contents)

# print out the common lines
for line in common_lines:
    print(line.strip() + " is present in both files")