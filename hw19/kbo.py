import matplotlib.pyplot as plt
import koreanize_matplotlib

def main():

    teams = ["LG", "SSG", "KIA", "NC", "두산", "삼성", "KT", "한화", "롯데", "키움"]
    win_rates = [0.622, 0.583, 0.570, 0.553, 0.540, 0.510, 0.488, 0.455, 0.430, 0.420]

    plt.bar(teams, win_rates, color="green")
    plt.ylim(0, 0.7)
    plt.title("2024년 KBO 팀별 승률")
    plt.xlabel("팀")
    plt.ylabel("승률")
    plt.savefig("kbo_winrates.png")
    plt.show()

if __name__ == "__main__":
    main()
