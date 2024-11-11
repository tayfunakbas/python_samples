import os

# file name with extension
file_name = os.path.basename('tayfun.txt')

# file name without extension
print(os.path.splitext(file_name)[0])
