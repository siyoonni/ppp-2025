height=int(input("키(m)가 얼마인가요?=>"))
weight=int(input("몸무게(kg)가 얼마인가요?=>"))
height_m=height/100
BMI=weight/pow(height_m,2)
print("BMI는{}입니다.".format(BMI))