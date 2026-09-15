# a = lambda x : x**2

# print(a(2))

# def sqaure(x):
#     return x ** 2


# l = [23, 34,5 ,5, 6, 22]
# # f = list(map(lambda x : x**2), l)
# # print(f)


# l1 = [1, 2, 3, 4, 5, 6, 7, 7, 8, 10]
# d = list(filter(lambda x : x%2!= 0, l1))
# q = map(lambda x: x**2, d)

# print(d)



a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

try:
    c = a / b
except (TypeError, NameError) as e:
    print(e)
else:
    print(c)
finally:
    print("It's all done")

