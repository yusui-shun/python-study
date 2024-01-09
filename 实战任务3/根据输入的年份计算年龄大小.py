# 开发人员    :  Yu
# 开发时间    : 2024/1/9  20:48
# 文件名称    : 根据输入的年份计算年龄大小.PY
# 开发工具    : PyCharm
import datetime
imyear=input("请输入你的出生年份： ")
nowyear=datetime.datetime.now().year
age=nowyear-int(imyear)
print("您的年龄为： "+str(age )+"岁")
if age<18:
    print("您现在为未成年人")
if age>=18 and age<=66:
    print("您现在为青年人")
if age>=66 and age<80:
    print("您现在为中年人")
if age>=80:
    print("您现在为老年人")

# 库存类主要的函数方法
# update改/更新
# find查找
# delete删除
# create添加
