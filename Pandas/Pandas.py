import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#series
#creation

city = ['kanpur', 'lucknow', 'agra', 'bareliy', 'unnao']
s_c = pd.Series(city)
print(s_c)


print(s_c.values)
print(s_c.index)



marks = [23, 24, 25, 26, 27, 30]
stu = ['s1', 's2', 's3', 's4', 's5', 's6']

stu_marks = pd.Series(marks, index=stu, name = "students ke marks")
print(stu_marks)

print(stu_marks.values)


subs = pd.read_csv("Pandas/pandas_visualization_practice.csv")
print(subs)

print("This is another record")

anothersub = pd.read_csv("Pandas/student_scores_only.csv")
print(anothersub)

print(type(subs))

#method

print(subs.head(4))

print(subs.tail())
print(subs.tail(2))

print(subs.sample(2))
print(subs.sort_index(ascending=False))

print(anothersub.sort_values(by="Score"))

print(subs.keys())
