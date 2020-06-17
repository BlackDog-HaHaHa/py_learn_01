# encoding=utf-8
# 反序列化

import pickle

pkl_file = open("data.pkl",'rb')

data0 = pickle.load(pkl_file)
data1 = pickle.load(pkl_file)
data2 = pickle.load(pkl_file)
data3 = pickle.load(pkl_file)

print(data0)
print(data1)
print(data2)
print(data3)

pkl_file.close()