# encoding:utf-8
# 序列化

import pickle

data0 = "hello world"
data1 = list(range(20))[1::2]
data2 = ("x","y","z")
data3 = {"a":data0,"b":data1,"c":data2}

print(data0)
print(data1)
print(data2)
print(data3)

output = open("data.pkl","wb")

pickle.dump(data0,output)
pickle.dump(data1,output)
pickle.dump(data2,output)
pickle.dump(data3,output)
output.close()