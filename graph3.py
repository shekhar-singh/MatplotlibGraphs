import matplotlib.pyplot as plt
year= [1995,1970,1990,2012]
pop= [2.11,3.15,4.151,2.22]

plt.scatter(year,pop)

plt.fill_between(year,pop,0,color='blue')
plt.show()
