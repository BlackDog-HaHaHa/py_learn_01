f = open("a.txt","r")   # f是一个文件句柄
f.seek(5)
print(f.read(1))
f.close()