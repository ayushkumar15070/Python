class outer:
    def __init__(self):
        self.name = "Outer"

    class inner:
        def __int__(self):
            self.name = "Inner"

        def display(self):
            print("This is the inner class")

Outer = outer()
print(Outer.name)

Inner = Outer.inner()

print(Inner.name)
print(Inner.display())