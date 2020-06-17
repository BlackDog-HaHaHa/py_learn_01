# -*- coding:utf-8 -*-

str = "我是中国人"
print(f'Unicode字符串为"{str}"')    # python3中定义默认编码就是Unicode

byte0 = str.encode("utf-8")
print(f'Unicode字符串"{str}"以utf-8编码得到字符串[{byte0}]')

str0 = byte0.decode("utf-8")
print(f'将utf-8字符串[{byte0}]以utf-8解码后得到字符串[{str0}]')

byte1 = str.encode("gbk")
print(f'Unicode字符串"{str}"以utf-8编码得到字符串[{byte1}]')

str1 = byte1.decode("gbk")
print(f'将utf-8字符串[{byte1}]以utf-8解码后得到字符串[{str1}]')

print(f'以文本的方式将Unicode字符串"{str}"写入a.txt')
with open("a.txt", "w", encoding="gbk") as f:
    f.write(str)

print(f'以文本方式读取a.txt的内容')
with open("a.txt", "r", encoding="gbk") as f:
    print(f.read())