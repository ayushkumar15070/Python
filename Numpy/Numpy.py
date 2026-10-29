import numpy as np

x = np.array([
    2, 3, 4, 5, 4,
    5, 2, 2, 1, 1,
    3, 4, 5, 5, 6,
    23, 23, 23, 23, 23
])

print(x)
print(type(x))

print(np.__version__)
print(np.array([1, 2, 2, 2, 2,2 ]))


#2D array 

a = np.array([[[[[[[
    [23, 23, 23, 23], 
    [23, 23, 23, 23], 
    [23, 23, 23, 23],
    [23, 23, 23, 23],
    [34, 34, 34, 34],
    [45, 45, 45, 45],
    [56, 56, 56, 56]
]]]]]]])


print(a)

print("\n")
print("This is another matrix")
print("\n")

s1 = np.array(
    [[[[[[[[
        [2, 3, 4, 5],
        [3, 3, 3, 3],
        [45, 45, 45, 45],
        [3, 3, 3, 3],
        [4, 4, 4, 4],
        [5, 5, 5, 5],
        [45, 45, 45, 45]
    ]]]]]]]], dtype=(complex))

print(s1)


