import random
from rich import print  

def check(solution, answer, input_ch):
    is_correct = False
    for i in range(len(solution)):
        if solution[i] == input_ch:
            answer[i] = solution[i]
            is_correct = True
    return is_correct

def main():
    priblems = ["apple", "banana"]
    solution = priblems[random.randrange(len(priblems))]
    solution = "apple"  
    is_correct = False
    lives = 5
    answer = ["_" for n in solution]

    while True:
        input_ch = input(f"{''.join(answer)}? ")

        if check(solution, answer, input_ch):
            print(f":white_check_mark: '{input_ch}'가 포함되어 있습니다.")
        else:
            lives -= 1
            print(f":x: '{input_ch}'는 포함되어 있지 않습니다. 남은 기회: {lives} :heart:")

        if "_" not in answer:
            is_correct = True
            break

        if lives < 0:
            break

        if is_correct:
            print(":white_check_mark: 잘하셨습니다.")
        else:
            print()  

        if answer == list(solution):
            print(":tada: 정답입니다.")
            is_correct = True
            break
        

if __name__ == "__main__":
    main()
