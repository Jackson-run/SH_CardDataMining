# -*- coding: utf-8 -*-
import pandas as pd
def today(x):
    return x.day
def tohour(x):
    return x.hour
def tominute(x):
    return x.minute
def toweekday(x):
    return x.isoweekday()
def tominutediv(x):
    return str(str(x.year)+"-"+str(x.month)+"-"+str(x.day)+"-"+str(x.hour)+"-"+str(x.minute/10+1))
def tominutedi(x):
    return str(x.minute/10+1)
def toisweekend(x):
    if x.isoweekday()/5==0:
        return 0
    else:
        return 1
def hourfenduan(x):
    y=str(x.year)
    m=str(x.month)
    d=str(x.day)
    h=x.hour
    if h>=0 and h<3:
        return y+m+'_'+d+'_'+'0'
    elif h>=3 and h<6:
        return y+m+'_'+d+'_'+'3'
    elif h>=6 and h<9:
        return y+m+'_'+d+'_'+'6'
    elif h>=9 and h<12:
        return y+m+'_'+d+'_'+'9'
    elif h>=12and h<15:
        return y+m+'_'+d+'_'+'12'
    elif h>=15and h<18:
        return y+m+'_'+d+'_'+'15'
    elif h>=18and h<21:
        return y+m+'_'+d+'_'+'18'
    else:
        return y+m+'_'+d+'_'+'21'
def parse(path):
    line = pd.read_csv(unicode(path, 'utf-8').encode('gbk'), encoding='gbk', header=None, names=['card_num', 'Date','Time', 'Bus_LineOrBgstation','Type', 'money', 'nature'])
    line.head(5)
    Taxi_Data = line[line.Type==str("出租").decode('utf-8')].drop(['card_num','Bus_LineOrBgstation','Type','nature'],1)
    Taxi_Data['recordtime']=pd.concat([Taxi_Data.Date+ " " + Taxi_Data.Time],axis = 1)
    Taxi_Data['recordtime']=pd.to_datetime(Taxi_Data['recordtime'],unit='ns')
    Taxi_Data['day']=Taxi_Data['recordtime'].map(today)
    Taxi_Data['hour']=Taxi_Data['recordtime'].map(tohour)
    Taxi_Data['minute']=Taxi_Data['recordtime'].map(tominute)
    Taxi_Data['weekday']=Taxi_Data['recordtime'].map(toweekday)
    Taxi_Data['Time_slot']=Taxi_Data['recordtime'].map(tominutediv)
    Taxi_Data['time_div'] = Taxi_Data['recordtime'].map(tominutedi)
    Taxi_Data['isWeekend']=Taxi_Data['recordtime'].map(toisweekend)
    from sklearn.preprocessing import MinMaxScaler
    Scaler = MinMaxScaler()
    Taxi_Data['weekday_cal']=Scaler.fit_transform(Taxi_Data[['weekday']])
    Taxi_Data['3hour']=Taxi_Data['recordtime'].map(hourfenduan)
    tianqi= pd.read_csv('/Users/wangrun/DataMining/f_tianqi.csv',encoding='utf-8')
    tianqi['time']=pd.to_datetime(tianqi['time'],unit='ns')
    tianqi['3hour']=tianqi['time'].map(hourfenduan)
    merge=pd.merge(Taxi_Data,tianqi,on='3hour',how='inner')
    merge.drop(['recordtime_y', 'name'],axis=1,inplace=True)
    Taxi_Data = merge.drop(['time','riqi','weekday_cal','3hour'],1)
    counts = merge.groupby(['Date','Time_slot']).size()
    t1=pd.DataFrame(counts)
    strl = '2015-04-'+path[-6:-4]
    a = t1.loc[strl][0]
    b = pd.Series(t1.loc[strl].index)
    c = pd.DataFrame(list(zip(a, b)))
    t=Taxi_Data['Date']
    s=t.drop_duplicates()
    stalist=list(s)
    lianjie = pd.DataFrame()
    for i in stalist:
        a = t1.loc[i][0]
        b = pd.Series(t1.loc[i].index)
        c = pd.DataFrame(list(zip(a, b)))
        c['new'] = c[1].map(lambda x: x+'-'+i)
        lianjie=pd.concat([lianjie,c],axis=0,ignore_index=True)
    Taxi_Data['new']=pd.concat([Taxi_Data.Time_slot+'-'+Taxi_Data.Date],axis=1)
    final = pd.merge(Taxi_Data,lianjie,on='new',how='inner')
    pd.DataFrame(final.drop(['new', 'Date', 'Time', 'money', 'recordtime_x', 'day', 'minute', 'Time_slot'], 1)).to_csv(
        '/Users/wangrun/data/Taxi-201504' + path[-6:-4] + '.csv')
def main():
    for i in range(1,31):
        if i<10:
            path_str = '0'+str(i)
        else:
            path_str = str(i)
        path = '/Users/wangrun/DataMining/card/SPTCC-201504'+path_str+'.csv'
        parse(path)
if __name__ == "__main__":
     main()


