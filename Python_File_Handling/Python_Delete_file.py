import os 

# os.remove("Python_File_Handling/Hello.py")

if os.path.exists("Python_File_Handling/DemoFile.txt"):
    os.remove("Python_File_Handling/DemoFile.txt")
else:
    print("File does not exist")


# this is used to remove the folder we can only remove the empty folders

os.rmdir("Python_File_Handling")  # but i can't remove this folder because this contains some of my important notes of python