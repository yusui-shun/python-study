# 开发人员    :  Yu
# 开发时间    : 2024/1/19  19:14
# 文件名称    : 简单取款机.PY
# 开发工具    : PyCharm
password = 0
i = 1
while i<7:
    num=input("请输入一位数字密码！")
    num=int(num)
    if num == password :
        print("密码正确,正进入系统!")
        i=7
    else:
        print("密码错误，已经输错 ",i,"次")
    i+=1
if i == 7:
    print("密码错误6次，请与发卡行联系")
