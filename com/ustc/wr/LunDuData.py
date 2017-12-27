import pandas as pd
base_path = '/Users/wangrun/DataMining/card/SPTCC-20150404.csv'
line = pd.read_csv(unicode(base_path, 'utf-8').encode('gbk'), encoding='gbk', header=None, names=['A', 'B', 'Time', 'D','Type', 'F', 'G'])
# data = line.drop(['A','B','G'],1)
Taxi = line.drop(['A','B','D','F','G'],1)
Taxi=Taxi[Taxi.Type==str('轮渡').decode('utf-8')]
lst = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(len(Taxi)):
    hour = int(str(Taxi.Time[i:i+1]).split(":")[0][-2:])
    lst[hour] = lst[hour]+1
print lst