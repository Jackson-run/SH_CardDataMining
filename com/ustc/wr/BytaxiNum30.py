# -*- coding:utf-8 -*-
import pandas as pd
lst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def getDataList(path_str):
    base_path = '/Users/wangrun/DataMining/card/SPTCC-201504' + path_str + '.csv'
    for i in range(1):
        line = pd.read_csv(unicode(base_path, 'utf-8').encode('gbk'), encoding='gbk', header=None, names=['A', 'B', 'Time', 'D','Type', 'F', 'G'])
        # data = line.drop(['A','B','G'],1)
        Taxi = line.drop(['A','B','D','F','G'],1)
        Taxi=Taxi[Taxi.Type == str("出租").decode("UTF-8")]
        if path_str<10:
            path_str = path_str[1:2]
            print path_str
        lst[int(path_str)]=len(Taxi)
    print lst
def main():
    for i in range(1,31):
        if i<10:
            path_str = '0'+str(i)
        else:
            path_str = str(i)
        getDataList(path_str)
    print lst
if __name__=="__main__":
    main()
