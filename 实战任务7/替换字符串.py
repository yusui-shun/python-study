# 开发人员    :  Yu
# 开发时间    : 2024/1/18  20:48
# 文件名称    : 替换字符串.PY
# 开发工具    : PyCharm
import re
pattern = r'1[34578]\d{9}'
string = '中奖号码为： 84978981 联系电话为： 13611111111'
result = re.sub(pattern,'1xxxxxxxxxx',string)
print(result)