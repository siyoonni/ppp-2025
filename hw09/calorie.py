def read_db(filename):
    calorie_dic={}
    with open (filename, encoding="utf-8-sig") as f:
        lines = f.readlines()

        for line in lines [1:]:
            line = line.strip()
            tokens=line.split(",")
            calorie_dic[tokens[0]] = int (tokens[1])

    return calorie_dic

def main():
    fruit_cal=read_db("./calorie_db.csv") 
    fruit_eat={"쑥": 150, "바나나": 200}
    total=0
    for item in fruit_eat:
        total+=(fruit_cal[item]*fruit_eat[item])
    print(f"총 칼로리는 {total}kcal입니다.")

if __name__ == "__main__":
    main()