arr = [3, 4, 5]
newarr = []
n = len(arr)

i = 0
while i < n:
    newarr.append(arr[i])
    i = i + 1

xor = newarr[0] ^ newarr[1]
xor2 = newarr[1] ^ newarr[2]
xor3 = newarr[0] ^ newarr[1] ^ newarr[2]

newarr.append(xor)
newarr.append(xor2)
newarr.append(xor3)

a = 0
b = a + 1

while a < len(arr):
    while b < len(arr):
        result = newarr[a] ^ newarr[b]
        b = b + 1
    a = a + 1

print(result)