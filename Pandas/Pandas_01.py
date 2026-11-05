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

print(ipl.dtypes)

print(ipl.isnull().sum())
print(ipl.info())

print(ipl.describe())

print(ipl.head())
print(ipl.tail())


print(ipl.sample(5))
print(ipl.sum())
print(stud.mean())

print(stud.sum(axis=1))

print(type(ipl[['City', 'Team1', 'ID']]))

print(ipl.iloc[0 :20: 2])
print(ipl['City'] == 'Ahmedabad')
print(ipl.iloc[0:4, 0:3])

print(ipl['City'] == 'Ahmedabad')
# Question_01 -> How many time chennai super kings has won the match in Kolkata
print("Chennai Super Kings matches won in Kolkata")

csk_kolkata = ipl[
    (ipl['WinningTeam'] == 'Chennai Super Kings') &
    (ipl['City'] == 'Kolkata')
]

print(csk_kolkata)
