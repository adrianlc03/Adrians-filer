import matplotlib.pyplot as plt
import numpy as np
def funk(x):
    R = 200000
    C = 100 * 10**-6
    return 9*(1-np.exp(-x/(R*C)))

x_1 = np.linspace(0,100,1000)
x_2 = [0,10,20,30,40,50,60,70,80,100]
y = [0, 3.7,5.76,6.9,7.66,8.12,8.36,8.56,8.72,8.9]
plt.plot(x_1,funk(x_1),"b",label= "Difflikning")
plt.plot(x_2,y,"r",label= "Målinger")
plt.xlabel("Tid [s]")
plt.ylabel("Spenning [V]")
plt.title("Difflikning vs Målinger")
plt.legend()
plt.savefig("Oblig_matte.png")
plt.show()
