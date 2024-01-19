# 开发人员    :  Yu
# 开发时间    : 2024/1/19  17:32
# 文件名称    : 除以判断.PY
# 开发工具    : PyCharm
print("今有物不知其数，三三数之剩二，五五之数剩三，七七数之剩二，问几何? \n")
number = int(input("请输入您认为符合条件的数："))
if number%3 == 2 and number%5 == 3 and number%7 == 2:
    print(number,"符合条件：三三数之剩二，五五之数剩三，七七数之剩二")