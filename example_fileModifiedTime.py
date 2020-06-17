# encoding=utf-8

import os
import datetime

print(f"当前时间：{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

for root,dirs,files in os.walk(r"d:\0"):
    # print(root)
    # print(dirs)
    # print(files)
    for file in files:
        absPathFile = os.path.join(root,file)
        # print(absPathFile)
        modifiedTime = datetime.datetime.fromtimestamp(os.path.getmtime(absPathFile))
        now = datetime.datetime.now()
        diffTime = now - modifiedTime
        print(
            f"{absPathFile:<50s}修改时间[{modifiedTime.strftime('%Y-%m-%d %H:%M:%S')}] 距今[{diffTime.days:3d}天{diffTime.seconds//3600:2d}时{(diffTime.seconds%3600)//60:2d}分]"
        )