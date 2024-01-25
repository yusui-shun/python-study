import math
def circlearea(r):
    result=math.pi*r*r
    return result
r = 10
print('半径为',r,'的圆面积为: ',circlearea(r))
r=10
result = lambda r:math.pi*r*r
print('半径为',r,'的圆面积为：',result(r))
