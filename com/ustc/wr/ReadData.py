# -*- coding:utf-8 -*-
import pandas as pd
#base_path = '/Users/wangrun/DataMining/card/SPTCC-20150404.csv'
def getDataList(base_path):
    line = pd.read_csv(unicode(base_path, 'utf-8').encode('gbk'), encoding='gbk', header=None, names=['A', 'B', 'Time', 'D', 'Type', 'F', 'G'])
    data = line.drop(['A','B','G','Type'],1)
    #print data[data.D==str("2号线南京东路").decode("utf-8")]

    #underground 为所有地铁数据
    #underground = data[data.Type==str("地铁").decode("utf-8")]
    #2号线和10号线到南京东路的数据
    _2line_nanjingdonglu = data[data.D==str("2号线南京东路").decode("utf-8")]
    _2line_nanjingdonglu = _2line_nanjingdonglu[_2line_nanjingdonglu.F>0]
    _10line_nanjingdonglu = data[data.D==str("10号线南京东路").decode("utf-8")]
    _10line_nanjingdonglu = _10line_nanjingdonglu[_10line_nanjingdonglu.F>0]
    #_merge2号线和10 号线
    _2_10_line_nanjingdonglu=_2line_nanjingdonglu.append(_10line_nanjingdonglu)
    lst = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(len(_2_10_line_nanjingdonglu)):
        hour = int(str(_2_10_line_nanjingdonglu.Time[i:i+1]).split(":")[0][-2:])
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
