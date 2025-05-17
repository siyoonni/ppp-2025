def main():
    numbers = []

    while True:
        x = input("X=? ")
        if x == "-1":
            break
        try:
            value = int(x)
            if value > 0:
                numbers.append(value)
        except:
            continue

    if numbers:
        avg = sum(numbers) / len(numbers)
    else:
        avg = 0

    print(f"입력된 값은 {numbers} 입니다. 총 {len(numbers)}개의 자연수가 입력되었고, 평균은 {avg:.1f}입니다.")

if __name__ == "__main__":
    main()
