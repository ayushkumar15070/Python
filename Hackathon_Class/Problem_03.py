string1 = "nagaram"
string2 = "anagram"


if len(string1) != len(string2):
    print(False)
else:
    string4 = sorted(string1)
    string5 = sorted(string2)
    if string4 == string5:
        print(True)
    else:
        print(False)

