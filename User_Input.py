# print("Enter your name: ")
# name = input()
# print(f"Hello {name}, how are you?")

# name = input("Enter you name: ")
# print(f"Hello {name}")

# fav1 = input("What is your favorite animal: ")
# fav2 = input("What is your favorite color: ")
# fav3 = input("What is your favorite number: ")
# print(f"Do you want a {fav2} {fav1} with {fav3} legs? ")


import math 
x = input("Enter the number of your choice: ")
y = math.sqrt(float(x))

print(y)

y = True
while y == True:
  x = input("Enter a number:")
  try:
    x = float(x)
    y = False
  except:
    print("Wrong input, please try again.")

print("Thank you!")