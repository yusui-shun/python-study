# 开发人员    :  Yu
# 开发时间    : 2024/1/19  17:22
# 文件名称    : 商品销售.PY
# 开发工具    : PyCharm
number = int(input("请输入商品7天销量:"))
if number >= 1000:
    print("本商品7天销量为A！")
elif number >= 500:
    print("本商品7天销量为B！")
elif number >= 300:
    print("本商品7天销量为C！")
else:
    print("本商品7天销量为D！")