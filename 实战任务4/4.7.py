# 开发人员    :  Yu
# 开发时间    : 2024/1/12  12:32
# 文件名称    : 4.7.PY
# 开发工具    : PyCharm
import random
INPUT=input("请输入操作命令：")
if INPUT == "摇一摇":
    ran = random.choice(('免单奖励','￥0.25'))
    print(ran)
else:
    print("error")