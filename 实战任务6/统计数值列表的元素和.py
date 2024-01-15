# 开发人员    :  Yu
# 开发时间    : 2024/1/15  15:14
# 文件名称    : 统计数值列表的元素和.PY
# 开发工具    : PyCharm
grade=[98,99,97,100,100,96,94,89,95,100]
total=sum(grade)
print("Python理论总成绩为：",total)
print("原列表：",grade)
grade.sort()
print("升序：",grade)
grade.sort(reverse=True)
print("降序：",grade)
char=['cat','Tom','Angle','pet']
char.sort()
print("区分字母大小写:",char)
char.sort(key=str.lower)
print("不区分字母大小写：",char)
grade_as=sorted(grade)
print("升序：",grade_as)
grade_des=sorted(grade,reverse=True)
print("降序：",grade_des)
print("原序列：",grade)
