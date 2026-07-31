def encode(message):
    string_of_A = 0
    string_of_B = 0
    string_of_C = 0
    for i in message:
        if i == "A":
            string_of_A = string_of_A + 1
        elif i == "B":
            string_of_B = string_of_B + 1
        else:
            string_of_C = string_of_C + 1

    return f"{string_of_A}A{string_of_B}B{string_of_C}C"




#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)