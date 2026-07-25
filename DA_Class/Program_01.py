list1 = input().split()


for i in list1:
    if "ayush" in list1:
        txt = "ayush"
        break


if "ayush" in list1:
    print(f"The name {txt} is present in {list1}")

print(list1)