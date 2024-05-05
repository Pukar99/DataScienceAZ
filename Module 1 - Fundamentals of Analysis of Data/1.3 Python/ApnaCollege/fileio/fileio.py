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

# f = open("sample1.txt", "a")
# f.write("I want to Learn javascript \n")
# f.close()

# #to overwrite at rist 
# f = open("sample1.txt", "r+")
# f.write("I want to Learn Pukar \n")
# f.close()

# with open("demo.txt", "r") as f:
#     data = f.read()
#     print(data)
#     print(type(data))
#     f.close()
    

# with open ("demo.txt", "w") as f:
#     f.write("I want to Learn Pukar very fast \n")
#     f.close()


#Q1. Create a new file "pracice.txt" and write "I am learning Python" in it.

# with open("practice.txt", "w") as f:
#     f.write("I am learning Python")
#     f.close()


#Q2. WAP that replace all occurences of java with python in above file.

# with open("practice.txt", "r+") as f:
#     data = f.read()
#     data = data.replace("Python", "Java")
# with open("practice.txt", "w") as f:
#     f.write(data)
#     f.close()
    
    
# Q3. find python in the senetences

with open("practice.txt", "r") as f:
    data = f.read()
    if "Python" in data:
        print("Yes")
    else:
        print("No")
    f.close()
    