# 开发人员    :  Yu
# 开发时间    : 2024/1/18  21:02
# 文件名称    : 正则表达式分割字符串.PY
# 开发工具    : PyCharm
import re
pattern = r'[?|&]'
url = 'http://ww.mingrisoft.com/login.jsp?username="mr"&pwd="mrsoft"'
result = re.split(pattern,url)
print(result)