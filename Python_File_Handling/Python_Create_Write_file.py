
with open("Python_File_Handling/DemoFile.txt", "a") as f:
    f.write("Hello everyone this is the new content which is being pushed into this file using python i didn't write anything in this file on my own it was all writen by the python itself.")

with open("Python_File_Handling/DemoFile.txt") as f:
    print(f.read())


with open("Python_File_Handling/DemoFile.txt", "w") as f:
    f.write("Hello everyone this is the content being written by the python but in this the previous content will be removed because we are using the w keyword in the attribute or setting so that we can override the previous content thank you.")


with open("Python_File_Handling/DemoFile.txt") as f:
    print(f.read())


f  = open("Python_File_Handling/Hello.py", "x")

with open("Python_File_Handling/Hello.py", "a") as f:
    f.write("print('Hello world')")

with open("Python_File_Handling/Hello.py") as f:
    print(f.read())


