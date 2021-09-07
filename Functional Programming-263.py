## 2. Comparing Object-Oriented to Functional ##

def read(filename):
    with open(filename, 'r') as f:
        return [line for line in f]
    
def count(lines):
    return len(lines)
    
example_lines = read('example_log.txt')
lines_count = count(example_lines)

## 4. The Lambda Expression ##

def read(filename):
    with open(filename, 'r') as f:
        return [line for line in f]
    
lines = read('example_log.txt')

sorted_lines = sorted(lines, key = lambda x: x.split(' ')[5])
print(sorted_lines)
                      