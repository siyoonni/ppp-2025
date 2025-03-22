import math
x=int(input("x 값을 입력하시오:"))
y=int(input("y 값을 입력하시오:"))
if x>0 and y>0:
    print("입력한 좌표는 1사분면입니다.")
elif x<0 and y>0:
    print("입력한 좌표는 2사분면입니다.")
elif x<0 and y<0:
    print("입력한 좌표는 3사분면입니다.")
elif x>0 and y<0:
    print("입력한 좌표는 4사분면입니다.")
elif x==0 and y==0:
    print("입력한 좌표는 원점입니다.")
elif x==0:
    print("입력한 좌표는 y축 위에 있습니다.")
elif y==0:
    print("입력한 좌표는 x축 위에 있습니다.")