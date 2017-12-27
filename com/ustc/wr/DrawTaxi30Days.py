import pandas as pd
import matplotlib.pyplot as plt
def main():
    file = open("/Users/wangrun/PycharmProjects/SH_CardDataMining/data/Taxi.txt")
    linenum = 0
    while 1:
        line = file.readline()
        linenum = linenum+1
        if not line:
            break
        lst = line.replace("[","").replace("]","").split(",")
        x1 = range(0, 24)
        y1 = lst
        plt.plot(x1, y1, label="April "+str(linenum)+", 2015line", linewidth=2, color='r', marker='o',
                 markerfacecolor='blue', markersize=6)
        plt.xlabel('TIME:0 to 23')
        plt.ylabel('ByTaxi_number')
        plt.title('data of ByTaxi_Number'+" April "+str(linenum)+", 2015")
        plt.legend()
        plt.show()
        #for i in range(len(lst)):
            #print int(lst[i])
if __name__=="__main__":
    main()
