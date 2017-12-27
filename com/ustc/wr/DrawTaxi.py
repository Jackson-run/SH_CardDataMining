import matplotlib.pyplot as plt
from matplotlib.pyplot import plot,savefig
x1=range(0,24)
y1=[4279, 2350, 1222, 627, 496, 1871, 8606, 12906, 12623, 13990, 14540, 14266, 14629, 16143, 15163, 15379, 14685, 14150, 13259, 14675, 15059, 13683, 10808, 6593]
x2 = range(0,24)
y2 = [6110, 3784, 2211, 1200, 1148, 3363, 6671, 10416, 14474, 15485, 15827, 15812, 16510, 17112, 17154, 16028, 15424, 16356, 14421, 13642, 13773, 13356, 9956, 6122]
plt.plot(x2,y2,label='April 4,ByTaxi_Num(Weekend)')
plt.plot(x1,y1,label="April 1,ByTaxi_Num(Working Day)",linewidth=2,color='r',marker='o',
markerfacecolor='blue',markersize=6)
plt.xlabel('TIME:0 to 23')
plt.ylabel('ByTaxi_number')
plt.title('Taxi_Time_Analyze')
plt.legend()
plt.show()