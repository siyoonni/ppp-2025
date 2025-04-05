def get_range_list(n):
    numbers=[]
    for i in range(1,n+1):
        numbers.append(i)
    return numbers

def main():
    num=5
    result=get_range_list(num)
    print("1부터 {}까지의 숫자 리스트는 다음과 같습니다:{}".format(num,result))

if __name__ == "__main__":
    main()