# 开发人员    :  Yu
# 开发时间    : 2024/1/19  17:24
# 文件名称    : 商品7天销量数据.PY
# 开发工具    : PyCharm
number = int(input("请输入商品7天销量："))
if number >= 1000:
    print("本商品7天销量为A！")
else:
    if number >= 500:
        print("本商品7天的销量为B")
    else:
        if number >= 300:
            print("本商品7天销量为C")
        else:
            print("本商品7天销量为D！")
