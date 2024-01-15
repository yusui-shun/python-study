# 开发人员    :  Yu
# 开发时间    : 2024/1/15  15:24
# 文件名称    : 列表推导式.PY
# 开发工具    : PyCharm
import random
randomnumber=[random.randint(10,100) for i in range(10)]
print("生成的随机数为：",randomnumber)
price = [1200,5330,2988,6200,1988,8888]
sale = [int(x*0.5) for x in price ]
print("原价格：",price)
print("打五折的价格：",sale)
sale1=[x for x in price if x>5000]
print("原列表：",price)
print("价格高于5000的：",sale1)