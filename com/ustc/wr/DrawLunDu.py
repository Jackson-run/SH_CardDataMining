import matplotlib.pyplot as plt
from matplotlib.pyplot import plot,savefig
x1=range(0,24)
y1=[49, 35, 22, 35, 216, 1210, 5797, 10249, 6735, 3351, 2593, 2339, 2462, 2545, 3033, 3783, 6173, 7401, 5026, 2635, 1866, 1186, 557, 247]
x2 = range(0,24)
y2 = [73, 31, 29, 31, 213, 863, 3239, 4440, 3110, 2362, 2175, 2241, 2501, 2700, 2885, 3165, 3703, 4439, 3406, 2368, 1854, 1155, 412, 165]
plt.plot(x2,y2,label='April 4,ByLunDu_Num(Weekend)')
plt.plot(x1,y1,label="April 1,ByLunDu_Num(Working Day)",linewidth=2,color='r',marker='o',
markerfacecolor='blue',markersize=6)
plt.xlabel('TIME:0 to 23')
plt.ylabel('ByLunDu_number')
plt.title('LunDu_Time_Analyze')
plt.legend()
plt.show()