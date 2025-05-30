import random
from rich import print  

def get_lotto():
    lotto_list = []
    while True:
        n = random.randint(1, 45)
        if n not in lotto_list:
            lotto_list.append(n)
        if len(lotto_list) == 6:
            break
    return sorted(lotto_list)

def main():
    for i in range(5):
        lotto_num = get_lotto()
        print(f":four_leaf_clover: 로또 번호 {i+1} :game_die: {lotto_num}")

if __name__ == "__main__":
    main()
