ipt = input("a.人民币 b.卢布\n  请输入要转换的币种序号：")
def exchange(RMB):
    return RMB*10
if ipt =="a":
    RMB=float(input('请输入要转换的人民币，退出输入0：'))
    while RMB:
        print('{0}元人民币={1}俄罗斯卢布'.format(RMB,exchange(RMB)))
        RMB=float(input('请输入要转换的人民币，退出输入0：'))

def unexchange(RUB):
    return RUB/10
if ipt =="b":
    RUB=float(input('请输入要转化的俄罗斯卢布，退出输入0：'))
    while RUB:
        print('{0}俄罗斯卢布={1}元人民币'.format(RUB,unexchange(RUB)))
        RMB=float(input('请输入要转换的俄罗斯卢布，退出输入0：'))