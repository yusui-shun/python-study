pf = set(['邓肯','加内特','马龙'])
print('大前锋位置的球员有：',pf,'\n')
cf = set(['邓肯','奥尼尔','姚明'])
print('中锋位置的球员有： ',cf, '\n')
print('交集运算',pf & cf)
print('并集运算:',pf | cf)
print('差集运算:',pf - cf)