# -*- coding:utf-8  -*-
for x in range(1,10):
    for y in range(1,x+1):
        print(f"{y}x{x}={x*y}".ljust(6),end=' ')
    print("")