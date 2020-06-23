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

# 按名称查找进程相关信息 2
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


# 杀死进程树
def kill_proc_tree(pid,sig=signal.SIGTERM,include_parent=True,
                   timeout=None,on_terminate=None):
    if pid == os.getpid():
        raise RuntimeError("I refuse to kill myself")
    parent = psutil.Process(pid)
    children = parent.children(recursive=True)
    if include_parent:
        children.append(parent)
    for p in children:
        p.send_signal(sig)
    gone, alive = psutil.wait_procs(children,timeout=timeout,callback=on_terminate)
    return gone,alive


# 杀死子进程
def reap_children(timeout=3):
    def on_terminate(proc):
        print("process {} terminated with exit code {}".format(proc,proc.returncode))
    procs = psutil.Process().children()
    # send SIGTERM
    for p in procs:
        p.terminate()
    gone,alive = psutil.wait_procs(procs,timeout=timeout,callback=on_terminate)
    if alive:
        for p in alive:
            print("process {} survived SIGTERM; trying SIGKILL" % p)
            p.kill()
        gone, alive = psutil.wait_procs(alive,timeout=timeout,callback=on_terminate)
        if alive:
            for p in alive:
                print("process {} survived SIGKILL; giving up" % p)