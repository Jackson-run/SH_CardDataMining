# -*- coding:utf-8 -*-
import pandas as pd
def getDataList(base_path):
    for i in range(1):
        line = pd.read_csv(unicode(base_path, 'utf-8').encode('gbk'), encoding='gbk', header=None, names=['A', 'B', 'Time', 'D','Type', 'F', 'G'])
        # data = line.drop(['A','B','G'],1)
        Taxi = line.drop(['A','B','D','F','G'],1)
        Taxi=Taxi[Taxi.Type == str("出租").decode("UTF-8")]
        lst = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for i in range(len(Taxi)):
            hour = int(str(Taxi.Time[i:i+1]).split(":")[0][-2:])
            lst[hour] = lst[hour]+1
        print lst
def main():
    for i in range(1,31):
        if i<10:
            path_str = '0'+str(i)
        else:
            path_str = str(i)
        path = '/Users/wangrun/DataMining/card/SPTCC-201504'+path_str+'.csv'
        getDataList(path)
if __name__=="__main__":
    main()
