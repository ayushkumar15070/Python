
Results_Of_Students = []
Student_names = ["Ayush Kumar Vishwakarma", "Ayush Kumar Pandey", "Ayush Kumar Gupta", "Ayush Kumar gupta", "Ayush Gupta", "Ayush Mishra" ]

while(True):
    marks1 = int(input("Enter your English marks: "))
    marks2 = int(input("Enter your Science marks: "))
    marks3 = int(input("Enter your Maths marks: "))
    marks4 = int(input("Enter your Hindi marks: "))
    marks5 = int(input("Enter your EVS marks: "))

    result = ((marks1 + marks2 + marks3 + marks4 + marks5)/500)*100

    if result > 95 and result < 100:
        print("Grade A")
        print(result)
    elif result > 80 and result < 95:
        print("Grade B")
        print(result)
    elif result > 75 and result < 80:
        print("Grade C")
        print(result)
    elif result > 60 and result < 75:
        print("Grade D")
        print(result)
    elif result > 50 and result <60:
        print("Grade E")
        print(result)
    else:
        print("Fail")
        print(result)

    Results_Of_Students.append(result)
    

    another = input("Do you want to perform more? Yes or no: ")
    if another.lower() == "yes":
        True
    else:
        see_the_result = input("Do you want to see the marks of students Yes or No: ")
        if see_the_result.lower() == "yes":
            for i in range((len(Results_Of_Students))):
                    print(f"The result of {Student_names[i]} is {Results_Of_Students[i]}")
            break
