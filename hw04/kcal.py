calories={"hallabong":50,"strawberry":34,"banana":77}


hallabong_g=int(input("한라봉 섭취량(g)을 입력하시오:"))
strawberry_g=int(input("딸기 섭취량(g)을 입력하시오:"))
banana_g=int(input("바나나 섭취량(g)을 입력하시오:"))


total_calories=calories["hallabong"]*hallabong_g/100+calories["strawberry"]*strawberry_g/100+calories["banana"]*banana_g/100

print("총 섭취한 칼로리는 {}입니다".format(total_calories))

