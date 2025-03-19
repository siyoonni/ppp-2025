import math
x1=int(input("x1 값을 입력하시오:"))
y1=int(input("y1 값을 입력하시오:"))
x2=int(input("x2 값을 입력하시오:"))
y2=int(input("y2 값을 입력하시오:"))
distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
print("(x1,y1)와 (x2,y2) 사이 거리는 {}입니다".format(distance))