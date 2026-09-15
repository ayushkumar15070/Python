# arr = [3, 4, 5]
# k = 2

# n = len(arr)
# newarr = []
# i = 0

# while i < k:
#     newarr.append(arr.pop())
#     i = i + 1

# newarr.extend(arr)

# print(newarr)


# queries = [1, 2]

# anotherarr = []
# for i in queries:
#     anotherarr.append(newarr[i])

# print(anotherarr)

# for i in anotherarr:
#     print(i)



# a = 5

# b = str(a*a)

# print(b)


# print(type(b))
# newstr = ""
# for i in b:
#     newstr = newstr + i

# print(newstr)

# sum = 0
# for i in newstr:
#     sum = int(i) + sum


# print(sum)

# if sum == a:
#     print("Yes they are Kaprekar ")
# else:
#     print("No they are not Kaprekar ")

# a = 45

# b = str(a * a)

# print(b)

# print(type(b))

# newstr = ""

# for i in b:
#     newstr = newstr + i

# print(newstr)

# digits = len(str(a))

# right = newstr[-digits:]
# print(right)
# left = newstr[:-digits]

# if left == "":
#     left = "0"

# sum = int(left) + int(right)

# print(sum)

# if sum == a:
#     print("Yes they are Kaprekar")
# else:
#     print("No they are not Kaprekar")

B = [4, 5, 6, 7]
loaves = 0
for i in range(len(B) - 1):
        if B[i] % 2 != 0:
            B[i] += 1
            B[i + 1] += 1
            loaves += 2

if B[-1] % 2 != 0:
    print("No")

print(str(loaves))