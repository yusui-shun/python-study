# 开发人员    :  Yu
# 开发时间    : 2024/1/19  17:57
# 文件名称    : 8.2.PY
# 开发工具    : PyCharm
import random
goods = [["sandisk 128G 优盘"],["Magic mouse2 鼠标",550],["罗技 mk235 键鼠套装",120],["小米 米家扫地机器人",1400]]
print(goods)
goodsel = list(random.choice(goods))
goodprince = int(goodsel[1])
print(goodsel[0])
for i in range(20):
    instr = input("请输入竞猜价格：")
    if int(instr)>goodprince:
        print("价格高了！")
    else:
        if int(instr)<goodprince:
            print("价格低了")
        else:
            print("恭喜你，你猜对了本商品的价格,你是大赢家!!")
            break;