# 开发人员    :  Yu
# 开发时间    : 2024/1/11  21:58
# 文件名称    : 3.4.PY
# 开发工具    : PyCharm
from datetime import datetime
day20=datetime.strptime('2024-11-11 0:0:0','%Y-%m-%d %H:%M:%S')
#设置未来时间
now=datetime.today()
delta=day20-now
day=delta.days
hour=int(delta.seconds /60 /60)
minutes=int((delta.seconds-hour*60*60)/60)
seconds=delta.seconds-hour*60*60-minutes*60
print('\033[31;43m 距离结束: \033[43m'+'\033[34;43m'+str(day)+'\033[43m'+'\033[31;43m天 \033[43m'+
      '\033[31;43m 距离结束: \033[43m'+'\033[34;43m'+str(hour)+'\033[43m'+'\033[31;43m小时 \033[43m'+
      '\033[31;43m 距离结束: \033[43m'+'\033[34;43m'+str(minutes)+'\033[43m'+'\033[31;43m分钟 \033[43m'+
      '\033[31;43m 距离结束: \033[43m'+'\033[34;43m'+str(seconds)+'\033[43m'+'\033[31;43m秒 \033[43m')

