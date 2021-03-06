# # -*- coding: utf-8 -*-
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib as mpl
#
#
# def draw_bar(labels, quants):
#     width = 0.4
#     ind = np.linspace(0.5, 9.5, 10)
#     # make a square figure
#     fig = plt.figure(1)
#     ax = fig.add_subplot(111)
#     # Bar Plot
#     ax.bar(ind - width / 2, quants, width, color='green')
#     # Set the ticks on x-axis
#     ax.set_xticks(ind)
#     ax.set_xticklabels(labels)
#     # labels
#     ax.set_xlabel('Country')
#     ax.set_ylabel('GDP (Billion US dollar)')
#     # title
#     ax.set_title('Top 10 GDP Countries', bbox={'facecolor': '0.8', 'pad': 5})
#     plt.grid(True)
#     plt.show()
#     plt.savefig("bar.jpg")
#     plt.close()
# labels = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30']
# quants = [252002, 239078, 279081, 266355, 229259, 236786, 255917, 256429, 262475, 288432, 297705, 265194, 256895, 256978, 214045, 247977, 291584, 303163, 256214, 243694, 252811, 252386, 265475, 287932, 297591, 263088, 251438, 262626, 241837, 277242]
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
Y = [5486612, 5389571, 5767164, 4260864, 3596383, 3442415, 5305808, 5666464, 5559211, 5933821, 4830799, 4403564, 5504892, 5493537, 5624940, 5541070, 5900202, 4729146, 4136843, 5438330, 5604199, 5591398, 5537694, 5840786, 4676876, 4271975, 5479664, 5434201, 5462398, 5788181]
fig = plt.figure()
plt.bar(X, Y, color="rgb")
plt.xlabel("Date(April)")
plt.ylabel("The number of by Bus")
plt.title("The change curve of Bus in 30 days")
plt.show()