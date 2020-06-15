# -*-coding: utf-8 -*-

arr = [1000000,600000,400000,200000,100000,0]  # 定义利润列表
rat = [0.01,0.015,0.03,0.05,0.075,0.1]  # 定义提成比例列表，与利润列表一一对应

while True:
    i = input('净利润（q退出）：')
    if i == 'q':
        exit(0)
    if not i.isdigit():
        continue
    reward = []
    print("奖金为：",end='')
    I = int(i)
    for idx in range(0,6):
        if I > arr[idx]:
            reward.append((I - arr[idx]) * rat[idx])
            I = arr[idx]
    reward.reverse()
    if len(reward) == 1:
        print(reward[0])
    else:
        print(" + ".join([str(num) for num in reward]),"=",sum(reward))