string1 = "ayush is the \t number {0} coder in the world, {1} {2}and also one more thing is that he can solve almost every problem in the world"
string2 = string1.replace("Ayush", "Rahul")
print(string2)

string3 = "Ayush"
for i in string3:
    print(i)

string4 = string3.center(34)
print(string4)

string5 = string1.upper()
print(string5)

string6 = string1.capitalize()
print(string6)

string7 = string1.count("i")
print(string7)

# string8 = string1.encode()
# print(string8)

word = "Straße"

print(word.lower())
print(word.casefold())

string9 = string1.endswith("d")
print(string9)

string10 = string1.find("ayush")
print(string10)

# this format replaces the {} (parenthesis from the value or parameter being provided by the user)
string11 = string1.format("one", "How are your", "What are you doing")
print(string11)


# We use this exapandtabs to give the tab spacing in the string whereever the \t is found in the string
string12 = string1.expandtabs()
print(string12)

string13 = string1.encode()
print(string13)
print(type(string13))

string14 = string1.format_map()
print(string14)

