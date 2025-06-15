def count_lines(filename):
    with open(filename, 'r') as file:
        return len(file.readlines())
    
print("Lines:", count_lines("example.txt"))