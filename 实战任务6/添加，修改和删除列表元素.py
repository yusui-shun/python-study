# 开发人员    :  Yu
# 开发时间    : 2024/1/15  14:43
# 文件名称    : 添加，修改和删除列表元素.PY
# 开发工具    : PyCharm
phone=["摩托罗拉","诺基亚","三星","OPPO"]
len(phone)
phone.append("iphone")
len(phone)
print(phone)
verse=["德国队小组赛回家","西班牙传控打法还有未来吗","C罗一人对抗西班牙队"]
print(verse)
verse[2]="梅西,C罗相约回家"
print(verse)
del verse[-1]
print(verse)
team=["火箭","勇士","开拓者","爵士","鹈鹕","马刺","雷霆","森林狼"]
value="公牛"
if team.count(value)>0:
    team.remove(value)
print(team)