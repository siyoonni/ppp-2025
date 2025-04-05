def average(nums):
    total = 0
    for n in nums:
        total = total + n
    return total / len(nums)

def main():
    input_text = input("숫자들을 한 줄로로 입력하세요(예시:10 20 30): ")
    tokens = input_text.split()
    numbers = []
    for token in tokens:
        numbers.append(int(token))
    
    result = average(numbers)
    print("입력한 숫자들의 평균은 {:.2f}입니다.".format(result))

if __name__ == "__main__":
    main()