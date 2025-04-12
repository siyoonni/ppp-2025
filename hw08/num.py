def main():
    with open("numbers2.txt", encoding="utf-8") as f:
        lines = f.readlines()

    nums = []
    for line in lines:
        line = line.strip()
        nums.append(int(line))

    nums.sort()

    count = len(nums)
    total = sum(nums)
    avg = total / count
    maximum = max(nums)
    minimum = min(nums)

    if count % 2 == 1:
        median = nums[count // 2]
    else:
        median = (nums[count // 2 - 1] + nums[count // 2]) / 2

    print("총 숫자 개수:", count)
    print("평균:", round(avg, 2))
    print("최댓값:", maximum)
    print("최솟값:", minimum)
    print("중앙값:", median)

if __name__ == "__main__":
    main()
