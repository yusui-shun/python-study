# 开发人员    :  Yu
# 开发时间    : 2024/1/19  17:48
# 文件名称    : 8.1.PY
# 开发工具    : PyCharm
number = input("支付宝支付密码：")
if number.isdigit():
    print("输入数字合法")
else:
    print("输入数字不合法，请重新输入！")
    number = input("支付宝支付密码: ")