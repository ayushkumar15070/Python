import os
import subprocess

print("""
What operation you want to perform:
1. Create and Write file
2. Delete file
""")

options = int(input("Enter your option: "))

name = input("Enter your file name: ")

if options == 1:
    if os.path.exists(f"{name}.py"):
        print("The file already exist")
    else:
        with open(f"{name}.py", "x") as f:
            pass

        wanttowritesomethingonthatfile = input("Do you want to write some program in that file (Yes or No): ")

        if wanttowritesomethingonthatfile.lower() == "yes":
            while True:
                value = input("").strip()
                if value == "exit":
                    break
                else:
                    with open(f"{name}.py", "a") as f:
                        f.write(f"{value}\n")
        else:
            print("Than you for working with us")

    wanttoseethecontentofthatfile = input("Want to see the content of that file (Yes or No): ")

    if wanttoseethecontentofthatfile.lower() == "yes":
        with open(f"{name}.py") as f:
            print(f.read())
    else:
        print("Thank you for working with us")

    wanttorunthatfile = input("Do you want to run that file as well (Yes or No): ")

    if wanttorunthatfile.lower() == "yes":
        print("This is the output of the file which you have created")
        subprocess.run(f"python {name}.py", shell = True)
    else:
        print("Thanks for working with us")
elif options == 2:
    os.remove(f"{name}.py")
else:
    print("Something is wrong")