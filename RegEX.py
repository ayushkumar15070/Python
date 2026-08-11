# A RegEX or regular expression is a sequence of characters that forms a seafch pattern

import re

txt = "The rain in Spain"
x = re.search("The rain", txt)

print(x)

x = re.findall("ai", txt)
print(x)


print(x)


z = re.split("\s", txt, 1)
print(z)


email = input("Enter your email: ")
pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

if re.fullmatch(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")

number = input("Enter your number: ")
numberpattern = r"[0-9]+"

if re.fullmatch(numberpattern, number):
    print("Valid Number")
else:
    print("Invalid Number")