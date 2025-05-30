import random
from rich import print  

def problem():
    dan = random.randint(1, 9)
    mul = random.randint(1, 9)

    try:
        ans = int(input(f"{dan} x {mul} = ? "))
    except ValueError:
        print(":no_entry: 숫자를 입력해주세요.")
        return False

    if ans == dan * mul:
        print(":white_check_mark: 정답입니다!\n")
        return True
    else:
        print(f":x: 오답입니다. 정답은 {dan * mul}입니다.\n")
        return False

def main():
    score = 0
    total_problem = 5

    print(":game_die: 구구단 퀴즈를 시작합니다!\n")

    for i in range(1, total_problem + 1):
        print(f"문제 {i}")
        if problem():
            score += 1

    print(f"\n총점은 {score}/{total_problem}점, {score/total_problem*100:.0f}점입니다! :trophy:")

if __name__ == "__main__":
    main()
