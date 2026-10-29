# # list1 = [1, 2, 3, 4, 4, 4, 5, 6, 6]
# # list2 = []

# # for i in list1:
# #     if list1.count(i) == 1:
# #         list2.append(i)
# #     else:
# #         pass

# # for i in list2:
# #     print(i)


# # #Another method
# # print("Another method")

# # list3 = [1, 2, 3, 4, 4, 5, 5, 5, 5,8, 9]

# # for i in list3:
# #     if list3.count(i) == 1:
# #         print(i)
# #     else:
# #         pass



# array = [1, 1, 2, 2, 2, 3, 3, 4, 5 ,7, 8, 10, 10]

# for i in range(len(array)):
#     if i in array:
#         print(f"{i} -> {array.count(i)}")
#     else:
#         pass


#Two sum
 

# s = "anagram"
# t = "nagaram"
# list1 = []
# list2 = []

# #First method
        
# if len(s) == len(t):
#     for i in s:
#         list1.append(i)

#     for i in t:
#         list2.append(i)

#     if(sorted(list1) == sorted(list2)):
#         print("yes they are anagram")
#     else:
#         print("No, they are not anagram")

# else:
#     print("No they are not anagram")


# #Second method
# print(sorted(s))
# if len(s) == len(t):
#     if(sorted(s) == sorted(t)):
#         print("Yes, they are anagram")
#     else:
#         print("No, they are not anagram")
# else:
#     print("No, they are not anagram")


