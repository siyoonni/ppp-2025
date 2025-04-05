def total_calorie(fruits, fruits_calorie_dic):
    total = 0
    for fruit in fruits:
        gram = fruits[fruit]
        kcal_per_100g = fruits_calorie_dic[fruit]
        total += gram * kcal_per_100g / 100
    return total

def main():
    fruits = {"딸기": 300, "한라봉": 150}
    fruits_calorie_dic = {"한라봉": 50, "딸기": 34, "바나나": 77}
    result = total_calorie(fruits, fruits_calorie_dic)
    print("총 섭취한 칼로리는 {:.1f}입니다.".format(result))

if __name__ == "__main__":
    main()