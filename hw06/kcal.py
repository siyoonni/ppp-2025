def total_calories(calories_dict):
    total = 0
    for fruit in calories_dict:
        grams = int(input(f"{fruit} 섭취량(g)을 입력하시오: "))
        total += calories_dict[fruit] * grams / 100
    return total

def main():
    calories = {"한라봉": 50, "딸기": 34,"바나나": 77}
    total = total_calories(calories)
    print("총 섭취한 칼로리는 {:.1f}입니다.".format(total))

if __name__ =="__main__":
    main()