import requests
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

def download_weather(station_id, year, filename):
    URL = f"https://api.taegon.kr/stations/{station_id}/?sy={year}&ey={year}&format=csv"
    with open(filename, "w", encoding="UTF-8-sig") as f:
        resp = requests.get(URL)
        resp.encoding = "UTF-8"
        f.write(resp.text)

def main():
    filename = "weather_146_2024.csv"
    download_weather(146, 2024, filename)

    df = pd.read_csv(filename, skipinitialspace=True)
    df["date"] = pd.to_datetime(df[["year", "month", "day"]])

    summer = df[df["month"].isin([6, 7, 8])]
    winter = df[df["month"].isin([12, 1, 2])]

    plt.hist(summer["tavg"], bins=20, color="red", alpha=0.6, label="여름")
    plt.hist(winter["tavg"], bins=20, color="blue", alpha=0.6, label="겨울")
    plt.legend()
    plt.xlabel("평균기온(℃)")
    plt.ylabel("일수")
    plt.title("2024년 여름과 겨울 평균기온 분포")
    plt.savefig("summer_winter_hist.png")
    plt.show()

if __name__ == "__main__":
    main()
