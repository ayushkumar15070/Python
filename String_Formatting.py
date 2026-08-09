name = input("Enter your name: ")


x = f"Hello how are you {name}"

print(x)
print("How can i help you? ")
print("Ask your doubt below: ")

chat = input()

if "fever" in chat.lower():
    print("""
            To cure fever here are some of the remedies you can follow if you are having a low fever
            1. Stay hydrated.
            2. Take Bed rest.
            3. Take DOLO 500 mg (if fever is high or you are having any pain).
            4. Seek doctor if you are having very heavy fever.
        """)
elif "How are you".lower() in chat.casefold():
    print(f"""I am Good how are you {name}""")
elif "Price".lower() in chat.casefold():
    print("What care price you want to know?")
else:
    print("Something is wrong")



y = 45
print(f"This product is {"Expensive" if y > 10 else "Cheap"}")