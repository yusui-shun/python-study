# 开发人员    :  Yu
# 开发时间    : 2024/1/15  16:18
# 文件名称    : 6.2.PY
# 开发工具    : PyCharm
currentWeekList=[4235,10111,8447,9566,9788,8951,9808]
LastWeekList=[4235,5612,8447,11250,9211,9985,3783]
AllList=currentWeekList+LastWeekList
print(AllList)
AllList.sort()
print(AllList)
AllList.sort(reverse=True)
print(AllList)
WeekList=["周日","周一","周二","周三","周四","周五","周六"]
Max=max(currentWeekList)
Min=min(currentWeekList)
WeekList.append(Max)
WeekList.append(Min)
print(WeekList)

