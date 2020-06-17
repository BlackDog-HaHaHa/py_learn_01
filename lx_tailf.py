# encoding=utf-8
# python实现Linux中tail -f的功能

import time

with open("a.txt",'rb') as f:
    f.seek(0,2)
    while True:
        line = f.read()
        if line:
            print(line.decode("utf-8"),end='')
        else:
            time.sleep(0.2)