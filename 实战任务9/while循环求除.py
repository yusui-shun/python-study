# 开发人员    :  Yu
# 开发时间    : 2024/1/19  19:21
# 文件名称    : while循环求除.PY
# 开发工具    : PyCharm
print("今有物不知其数，三三之数剩二，五五数之剩三，七七数之剩二，问几何？\n")
none = True
number = 0
while none:
     number +=2
     if number%3==2 and number%5==3 and number%7 ==2:
         print("答曰:这个数是",number)
         none=False