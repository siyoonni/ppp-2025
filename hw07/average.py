def average(nums):
    total=0
    for n in nums:
        total=total+n
    return total/len(nums)

def main():
    numbers=[10,20,30,40,50]
    result=average(numbers)
    print("입력한 리스트의 평균은 {:.2f}입니다.".format(result))

if __name__ == "__main__":
    main()