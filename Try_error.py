x = 10

try:
    print(x)
    print("Hey the value of x is avilable in the database!")
except:
    print("Hey what are you doing x is not defined!!!")


try:
    f = open("trial.txt")
    try:
        f.write("Hello Everyone")
    except:
        print("Something went wrong while writing in file")
    finally:
        f.close()
except:
    print("Something went wrong while opening the trail.txt file")
