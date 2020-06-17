# 两种方式输出3和5，3变apple，5变orange，公约数变appleorange

# 第一种
for i in range(1,21):
    print("apple"[i%3*5:]+"orange"[i%5*6:] or i)

# 第二种
print("\n".join([str("apple"[i%3*5:]+"orange"[i%5*6:] or i) for i in range(1,21)]))