#Creation
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

marks = [
    [45, 34, 41, 26, 47],
    [32, 23, 34, 45, 23],
    [12, 23, 34, 45, 45],
    [45, 45, 45, 45, 45]
]

student = pd.DataFrame(marks, columns= ['S1', 'S2', 'S3', 'S4', 'S5'])

print(student)


marks1 = {
    'name':['Ayush', 'Chitransh', 'Ayush', 'Unnat','Anurag'],
    'S1':[45, 56, 34, 23, 23],
    'S2':[34, 12, 23, 45, 56],
    'S3':[12, 23, 23, 34, 45],
    'S4':[56, 56, 56, 56, 56]
}

stud = pd.DataFrame(marks1)

print(stud)

stud.set_index('name', inplace=True)
print(stud)

ipl = pd.read_csv("Pandas/ipl-matches.csv")
print(ipl)
