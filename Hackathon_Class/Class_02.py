nums = list(map(int, input().split()))
k = int(input())
nums.sort(reverse=True)
j = 1

for i in nums:
    if j == k:
        print(nums)
        print(i)
        break
    j = j + 1
