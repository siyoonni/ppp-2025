import math
r=int(input("반지름을 입력하시오:"))
pi=math.pi
formula=2*pi*r
area=pi*r**2

print(f"반지름이{r}인 원의 둘레는{formula:.1f}입니다.")
print(f"반지름이{r}인 원의 면적은{area:.2f}입니다.")