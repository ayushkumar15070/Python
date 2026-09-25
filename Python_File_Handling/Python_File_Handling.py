f = open("Python_File_Handling/DemoFile.txt")

print(f.read())

print(f.readline())
f.close()

with open("Python_File_Handling/DemoFile.txt") as f:
    print(f.read())

with open("Python_File_Handling/DemoFile.txt") as f:
    print(f.read(43))

