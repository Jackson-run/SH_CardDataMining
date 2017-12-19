import matplotlib.pyplot as plt
from matplotlib.pyplot import plot,savefig
x1=range(0,24)
x2 = range(0,24)
y2=[0, 0, 0, 0, 0, 25, 386, 1181, 2888, 3512, 4290, 5090, 4971, 6119, 6090, 5260, 4921, 4523, 3764, 2987, 2027, 1080, 676, 124]
y1=[0, 0, 0, 0, 0, 28, 637, 3772, 15321, 9424, 4245, 3251, 3263, 3732, 3627, 3050, 3029, 3753, 5326, 2874, 1528, 1073, 829, 177]
plt.plot(x1,y1,label="April 3, 2015line",linewidth=2,color='r',marker='o',
markerfacecolor='blue',markersize=6)
plt.plot(x2,y2,label='April 4, 2015line')
plt.xlabel('TIME:0 to 23')
plt.ylabel('nanjingdonglu_number')
plt.title('data of nanjingdonglu station')
plt.legend()
plt.show()
plt.savefig('test.jpg')
