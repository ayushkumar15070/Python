import os

i = int(input("how many files you wanna delete: "))

a = 0

while a <= i:
    # if os.path.exists(f"hello{a}"):
    os.remove(f"hello{a}.py")
    # else:
        # print("The file doesn't exist/ anymore")

    a = a + 1

# os.remove("hello0.py")