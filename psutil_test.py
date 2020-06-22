import os
import psutil
import signal

# 按名称查找进程相关信息 1
def find_procs_by_name_1(name):
    "Return a list of processes matching 'name'."
    ls = []
    for p in psutil.process_iter(attrs=['name']):
        # print(p)
        # print(p.info['name'])
        if p.info['name'] == name:
            ls.append(p)
    # print(ls)
    return ls

# a = find_procs_by_name_1('TIM.exe')
# print(a)


def find_procs_by_name_2(name):
    ls = []
    for p in psutil.process_iter(attrs=["name","exe","cmdline"]):
        if name == p.info['name'] or \
            p.info['exe'] and os.path.basename(p.info['exe']) == name or \
            p.info['cmdline'] and p.info['cmdline'][0] == name:
            ls.append(p)
    return ls

# a = find_procs_by_name_2('TIM.exe')
# print(a)