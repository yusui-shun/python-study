# 开发人员    :  Yu
# 开发时间    : 2024/1/13  19:48
# 文件名称    : 参与手机店的打折活动.PY
# 开发工具    : PyCharm
print("\n手机店正在打折，活动进行中。。。")
strweek=input("请输入中文星期：")
inttime=int(input("请输入时间中的小时："))
if(strweek=="星期二"and(inttime>=10 and inttime <=11)) \
    or(strweek=="星期五" and (inttime>=14 and inttime <=15)):
    print("恭喜您，活得了折扣活动参与资格，快快选购把")
else:
    print("对不起，您来晚一步，期待下次活动")