# # File I/O in Python
# # Python can be used to perform operations on a file.
# # File operations are read, write, append, and delete.
# # Types of all files:
# # 1. Text files (txt, csv, etc.)
# # 2. Binary files (mp4, mp3, pdf, etc.)
# # 3. JSON files

# # f = open("file_name", "mode")
# # modes: r, w, a, r+, w+, a+
# # r: read
# # w: write
# # a: append
# # r+: read and write
# # w+: write and read
# # a+: append and read

# # data = f.read()
# # f.close()

# # f = open("demo.txt", "r")
# # data = f.read()
# # print(data)
# # print(type(data))
# # f.close()

# # Output: Pukar

# f = open("demo.txt", "r")
# data = f.read(2)
# print(data)
# f.close()


# f = open("demo.txt", "r")
# line1 = f.readline()
# line2 = f.readline()
# print(line1)
# print(line2)
# f.close()

# # Read () and Readline() are used to read the file.
# # Read() reads the whole file.
# # Readline() reads the first line of the file.

# f = open("demo.txt", "a")
# f.write("I want to Learn javascript \n")
# f.close()

f = open("sample1.txt", "a")
f.write("I want to Learn javascript \n")
f.close()
