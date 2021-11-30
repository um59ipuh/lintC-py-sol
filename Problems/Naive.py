import sys


# 2097 · Find the sum of two parameters
# read two parameters from command like `python main.py 1 2` by sys.argv
# a, b = sys.argv[1], sys.argv[2]
# total = plus(int(a), int(b))
# print(total)

# 2098 · Read the values in the file and sum them
input_filepath = sys.argv[1]
# write your code here to read file content
with open(input_filepath) as f:
    nums = f.readlines()[0].split()
    a, b = int(nums[0]), int(nums[1])
    print(a + b)

# 2105 · Write Hello World! in the file
def write_to_file(filepath):
    with open(filepath, 'w') as f:
        s = "Hello World!"
        f.write(s)


# 2106 · Create a file directory and write Hello World!
import os
def write_to_file(f):
    d = os.path.dirname(f)
    os.makedirs(d, exist_ok=True)
    with open(f, 'w') as f:
        f.write('Hello World!')

if __name__ == '__main__':
    pass