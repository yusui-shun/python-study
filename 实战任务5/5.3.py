# 开发人员    :  Yu
# 开发时间    : 2024/1/14  18:27
# 文件名称    : 5.3.PY
# 开发工具    : PyCharm
number1=int(input("请输入加油的钱数："))
number2=int(input("请输入运行的公里数："))
c=number1/number2
print("您车辆的每公里的油耗为：",c)
number3=int(input("请输入车辆1年运行的总公里数："))
print("您的车辆一年的油费为：",int(c*number3))