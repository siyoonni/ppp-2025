hallabong_cal=50
strawberry_cal=34
banana_cal=77

hallabong_g=int(input("한라봉 섭취량(g)을 입력하시오:"))
strawberry_g=int(input("딸기 섭취량(g)을 입력하시오:"))
banana_g=int(input("바나나 섭취량(g)을 입력하시오:"))

total_cal=(50*hallabong_g/100)+(34*strawberry_g/100)+(77*banana_g/100)

print("총 섭취한 칼로리는 {}입니다".format(total_cal))