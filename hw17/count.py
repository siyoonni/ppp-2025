import time
from rich import print

def count_down(count):
    for n in range(count):
        print(f"{count - n}...", end="\r")
        time.sleep(1)
    print(":bomb: Boom!!")

def main(): 
    count_down(3)

if __name__ == "__main__":
    main()
