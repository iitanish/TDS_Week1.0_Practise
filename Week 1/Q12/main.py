import pandas as pd
data1=pd.read_csv("data1.csv",encoding="cp1252")
data2=pd.read_csv("data2.csv",encoding="utf8")
data3=pd.read_csv("data3.txt",sep="\t",encoding="utf16")
conbined_data=pd.concat([data1,data2,data3],axis=0,ignore_index=True)
filtered_data=conbined_data[conbined_data['symbol'].isin(["“","Œ","ƒ"])]
print(filtered_data['value'].sum())
print(conbined_data)
