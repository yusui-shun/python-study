# 开发人员    :  Yu
# 开发时间    : 2024/1/12  12:22
# 文件名称    : 4.5.PY
# 开发工具    : PyCharm
import os
print("1.石头  2.剪子  3.布")
number1=int(input("请输入1or2or3："))
os.system("cls")
number2=int(input("请输入1or2or3："))
if number1 == number2:
    print("平")
if number1==1 and number2==2:
    print("第一位玩家赢")
if number1==1 and number2==3:
    print("第二位玩家赢")
if number1==2 and number2==1:
    print("第二位玩家赢")
if number1==2 and number2==3:
    print("第一位玩家赢")
if number1==3 and number2==1:
    print("第一位玩家赢")
if number1==3 and number2==2:
    print("第二位玩家赢")