def fun_checkout(name):
    nickname=""
    if name == "邓肯":
        nickname = "石佛"
    elif name == "吉诺比利":
        nickname = "妖刀"
    elif name == "罗宾逊":
        nickname = "海军上将"
    else:
        nickname = "无法找到您输入的信息"
    return nickname
#调用函数



while True:
    name = input("请输入NBA球星名称")
    nickname = fun_checkout(name)
    print("球员",name,"绰号",nickname)

