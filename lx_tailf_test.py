import time

f = open("a.txt","a")   # f是一个文件句柄

for i in range(1,10):
    f.write("\ntest"+str(i))
    f.flush()   # 只有每次都强制写入磁盘，才能看出效果
    time.sleep(2)
f.close()