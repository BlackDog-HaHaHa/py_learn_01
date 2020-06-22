import os
import psutil
import signal

# 按名称查找进程相关信息 1
def find_procs_by_name(name):
    "Return a list of processes matching 'name'."
    ls = []
    for p in psutil.process_iter(attrs=['name']):
        # print(p)
        if p.info['name'] == name:
            ls.append(p)
    # print(ls)
    return ls

find_procs_by_name("TIM.exe")
