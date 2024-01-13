# 开发人员    :  Yu
# 开发时间    : 2024/1/13  19:58
# 文件名称    : 5.1.PY
# 开发工具    : PyCharm
i=1
while i<4:
    number=input("输入数字")
    type=input("输入当前数字的进制类型：")
    if type=="8" or type=="2" or type=="16":
        if type == "8":
            num8=int(number,8)
            print("8进制267的十进制为",num8)
        if type == "2":
            num2=int(number,2)
            print("2进制10110001的十进制为", num2)
        if type == "16":
            num16=int(number,16)
            print("16进制e3a5的十进制为", num16)
    else:
        print("请输入正确的数字")