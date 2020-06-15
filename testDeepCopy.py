# encoding=utf-8

# 深复制

import copy

object1 = ["will", 28, ["python", "c#", "JavaScript"]]
object2 = copy.deepcopy(object1)

print(f"id of objectl {id(object1)}")
print(object1)
print([id(ele) for ele in object1])

print(f"id of object2 {id(object2)}")
print(object2)
print([id(ele) for ele in object2])

# 尝试修改object1，然后看object2的变化

object1[0] = "wilber"
object1[2].append("CSS")

print("更改后的变化")

print(f"id of objectl {id(object1)}")
print(object1)
print([id(ele) for ele in object1])

print(f"id of object2 {id(object2)}")
print(object2)
print([id(ele) for ele in object2])