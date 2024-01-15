# 开发人员    :  Yu
# 开发时间    : 2024/1/15  16:01
# 文件名称    : 元组推导式.PY
# 开发工具    : PyCharm
import random
randomnumber=(random.randint(10,100) for i in range(10))
randomnumber = tuple(randomnumber)
print("生成的元组为：",randomnumber)
number=(i for i in range(3))
print(number.__next__())
print(number.__next__())
print(number.__next__())
number=tuple(number)
print("转换后：",number)
number1=(i for i in range(4))
for i in number1:
    print(i,end=" ")
print(tuple(number))