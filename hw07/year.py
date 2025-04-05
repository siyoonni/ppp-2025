def is_leap_year(y):
    if y % 4 == 0:
        if y % 100 == 0:
            return False
        else:
            return True
    else:
        return False

def main():
    year = int(input("연도를 입력하세요: "))
    print(is_leap_year(year))

if __name__ == "__main__":
    main()