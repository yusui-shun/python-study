# 开发人员    :  Yu
# 开发时间    : 2024/1/18  20:04
# 文件名称    : 去掉字符串空格.PY
# 开发工具    : PyCharm
str1=' http://www.mingrisoft.com   \t\n\r'
print('原字符串str1: ' + str1 + '. ')
print('字符串: ' + str1.strip() + '。 ')
str2='@明日科技.@.'
print('原字符串str2:  '+ str2 +'. ')
print('字符串: ' + str2.strip('@.') + '。 ')

str1=' http://www.mingrisoft.com   \t\n\r'
print('原字符串str1: ' + str1 + '. ')
print('字符串: ' + str1.strip() + '。 ')
str2='@明日科技.@.'
print('原字符串str2:  '+ str2 +'. ')
print('字符串: ' + str2.lstrip('@.') + '。 ')

str1=' http://www.mingrisoft.com   \t\n\r'
print('原字符串str1: ' + str1 + '. ')
print('字符串: ' + str1.strip() + '。 ')
str2='@明日科技.@.'
print('原字符串str2:  '+ str2 +'. ')
print('字符串: ' + str2.rstrip('@.') + '。 ')

