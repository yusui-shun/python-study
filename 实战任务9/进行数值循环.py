# 开发人员    :  Yu
# 开发时间    : 2024/1/19  19:08
# 文件名称    : 进行数值循环.PY
# 开发工具    : PyCharm
for i in [1,2,3]:
    print("笑傲江湖")
for i in ["明日","科技","与您","同行"]:
    print(i)
print("计算1+2+3+...+100的结果为:")
result = 0
for i in range(101):
    result += i
print(result)
for i in range(1,10,2):
    print(i,end = ' ')
string = '天道酬勤'
print(string)
for ch in string:
    print(ch)
i =1
while i<=3:
    print("笑傲江湖")
    i=i+1