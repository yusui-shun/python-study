# 开发人员    :  Yu
# 开发时间    : 2024/1/18  19:37
# 文件名称    : 分割字符串.PY
# 开发工具    : PyCharm
str1='明日学院官网 >>> www.mingrisoft.com'
print('原字符串:' ,str1)
list1=str1.split()
list2=str1.split('>>>')
list3=str1.split('.')
list4=str1.split(' ',4)
print(str(list1)+'\n'+str(list2)+'\n'+str(list3)+'\n'+str(list4))
list5=str1.split('>')
print(list5)
