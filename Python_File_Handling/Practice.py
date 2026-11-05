
i = int(input("How many files you wanna create: "))

a = 0

while a <= i:
    with open(f"hello{a}.py", "x") as f:
        f.write(f"print(\"Hello world{a}\")")

    a = a + 1

