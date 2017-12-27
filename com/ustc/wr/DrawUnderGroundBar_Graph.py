# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
Y = [9024322, 8971554, 9573353, 6162358, 5385069, 5029067, 8652931, 9020362, 8995980, 9702825, 7099529, 6302968, 8893497, 8855561, 9089193, 9005794, 9690765, 6902697, 5826715, 8772735, 9073352, 9189315, 9122676, 9672277, 7119010, 6306224, 8909261, 9017493, 8962468, 9692404]
fig = plt.figure()
plt.bar(X, Y, color="rgb")
plt.xlabel("Date(April)")
plt.ylabel("The number of by UnderGround")
plt.title("The change curve of UnderGround in 30 days")
plt.show()