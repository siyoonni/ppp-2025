def c2f(t_c):
    return t_c * 9 / 5 + 32

def main():
    temp_c = 26.7
    temp_f =c2f(temp_c)

    print(f"{temp_c}C => {temp_f}F")

if __name__ =="__main__": 
    main()