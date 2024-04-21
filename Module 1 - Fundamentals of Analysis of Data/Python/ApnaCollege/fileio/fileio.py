#File I/O in Python
#Python can be used to perform operations on a file.
#File operations are read, write, append, and delete.
#Types of all files:
#1. Text files (txt, csv, etc.)
#2. Binary files (mp4, mp3, pdf, etc.)
#3. JSON files

# f = open("file_name", "mode")
# modes: r, w, a, r+, w+, a+
# r: read
# w: write
# a: append
# r+: read and write
# w+: write and read
# a+: append and read

# data = f.read()
#f.close()

f = open("demo.txt", "r")
data = f.read()
print(data)
f.close()

#Output: Hello, this is a demo file.
