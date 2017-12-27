import matplotlib.pyplot as plt
from matplotlib.pyplot import plot,savefig
x1=range(0,24)
x2 = range(0,24)
y2=[0, 0, 0, 0, 0, 141, 542, 1298, 2169, 1794, 1855, 2347, 2636, 3106, 3287, 3787, 5037, 11210, 9660, 4958, 4827, 4137, 1923, 46]
y1=[0, 0, 0, 0, 0, 28, 637, 3772, 15321, 9424, 4245, 3251, 3263, 3732, 3627, 3050, 3029, 3753, 5326, 2874, 1528, 1073, 829, 177]
plt.plot(x1,y1,label="April 1, 2015line_njdl_end",linewidth=2,color='r',marker='o',
markerfacecolor='blue',markersize=6)
plt.plot(x2,y2,label='April 1, 2015line_njdl_start')
plt.xlabel('TIME:0 to 23')
plt.ylabel('nanjingdonglu_number')
plt.title('data of nanjingdonglu station')
plt.legend()
plt.show()
plt.savefig('test.jpg')
