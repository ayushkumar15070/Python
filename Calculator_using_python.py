# Calculator using operators

while(True):
    print("""
    ----------- What operation do you wanna perform-----------
                    1. Addition
                    2. Multiplication
                    3. Subtraction
                    4. Division
    """)

    operation = int(input("Enter the option: "))
    if operation > 4:
        print("Enter valid option: ")
        True
    else:
        if (operation == 1):
            while(True):
                x = int(input("Enter any number: "))
                y = int(input("Enter any number: "))
                z = x + y
                txt = f"The sum of {x} + {y} = {z}"
                print(txt)
                Close = input("Do you wanna perform more addition operation answer in yes or no: ")
                if (Close.lower() == "no"):
                    break
                else:
                    True
            
        elif(operation == 2):
            while(True):
                x = int(input("Enter any number: "))
                y = int(input("Enter any number: "))
                z = x * y
                txt = f"The sum of {x} X {y} = {z}"
                print(txt)
                Close = input("Do you wanna perform more Multiplication operation answer in yes or no: ")
                if (Close.lower() == "no"):
                    break
                else:
                    True

        elif(operation == 3):
            while(True):
                x = int(input("Enter any number: "))
                y = int(input("Enter any number: "))
                z = x - y
                txt = f"The sum of {x} - {y} = {z}"
                print(txt)
                Close = input("Do you wanna perform more Subtraction operation answer in yes or no: ")
                if (Close.lower() == "no"):
                    break
                else:
                    True

        elif(operation == 4):
            while(True):
                x = int(input("Enter any number: "))
                y = int(input("Enter any number: "))
                z = float(x / y)
                txt = f"The sum of {x} / {y} = {z}"
                print(txt)
                Close = input("Do you wanna perform more Division operation answer in yes or no: ")
                if (Close.lower() == "no"):
                    break
                else:
                    True
        else:
            print("Enter the valid number")
            True

        anotheroperation = input("Do you wanna perform any more operation answer in yes or no: ")
        if (anotheroperation.lower() == "no"):
            break
        else:
            True
