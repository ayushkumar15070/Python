import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.array([0, 6])
y = np.array([0, 250])

plt.plot(x, y)

plt.show()

#Python Class Work 
price = [23000, 23000, 45000, 89000, 9000]
otherprice = [21000, 23000, 34000, 45000, 23000]
year = [2016, 2017, 2018, 2019, 2020]

plt.plot(year, price, color = 'r', linestyle = 'dashed', linewidth = 2, marker = "d", markersize = 5 , label = 'Com 1')
plt.plot(year, otherprice, color = 'g', linestyle = 'solid', linewidth = 2, marker = "o", markersize = 10 , label = 'Com 2')

plt.xlabel("Year")
plt.ylabel("Price")
plt.grid()
plt.legend(loc = 'best')
plt.title("Price Analysis", color='blue', fontsize=15, fontstyle = 'italic', fontweight='bold', fontfamily = 'Verdana')
# plt.xlim(10, 1000)
# plt.ylim(18000, 35000)
plt.show()


stat = pd.read_csv("Python_Matplotlib/kohli_rohit_scores_2010_2020.csv")

print(stat)

year = stat['Year']
RSharma = stat['R_Sharma_Runs']
V_Kohli = stat['V_Kohli_Runs']

plt.plot(year, RSharma, color='g', linestyle='dashed', linewidth=1, marker='d', markersize=5, label='Rohit Sharma')

plt.plot(year, V_Kohli, color='r', linestyle='solid', linewidth=1, marker='o', markersize=5, label='Virat Kohli')

plt.xlabel("Year")
plt.ylabel("Runs Scored")

plt.title("Rohit Sharma vs Virat Kohli")

plt.grid()
plt.legend(loc='best')

plt.show()


language = ['Python', 'C++', 'C', 'Java']
popularity = [85, 60, 40, 30]
c = ['r', 'g', 'y', 'b']

plt.bar(language, popularity, color = c, width=8, alpha= 0.7, edgecolor = 'k', linewidth = 2, label = 'Popularity')

plt.xlabel('Languages', fontsize = '19', weight = 'bold', style = 'italic')
plt.ylabel('Popularity', fontsize = '20', weight = 'bold', style = 'italic')
plt.title("Popularity of Praogmming Languages", fontsize = '20', weight = 'bold')
plt.legend()
plt.grid()
plt.show()