def sum_n(n):
    total=0
    for i in range(1,n+1):
        total += i
    return total

def main():
    n=int(input("숫자 n을 입력하세요:"))
    result=sum_n(n)
    print(f"1부터 {n}까지의 합은 {result}입니다.")

if __name__ =="__main__":
    main()