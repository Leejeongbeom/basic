import matplotlib.pyplot as plt

x=['A','B','C','D','E','F']
y=[13,17,20,5,2,4]
y2 = [5,10,15,7,1,19]
plt.xlabel("Eng")
plt.ylabel("Number")
plt.plot(x,y,label='orange')
plt.plot(x,y2,label='blue')
plt.legend(loc="upper left")

plt.show()