# 开发人员    :  Yu
# 开发时间    : 2024/1/19  16:04
# 文件名称    : 彩票中奖.PY
# 开发工具    : PyCharm
number= int(input("请输入您的6位奖票号码"))
if number == 432678:
    print(number,"你中了本期大奖，请速来领奖！！")
if number != 432678:
    print(number,"你未中了本期大奖")
data = 105
if data >= 100:
    print(data,"此商品为A类商品")
data = 65
if data <= 100:
    print(data,"此商品为B类商品")
