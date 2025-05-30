import requests
import pandas as pd
from sfarm_hw import submit_to_api  

def download_weather(station_id, year, filename):
    URL = f"https://api.taegon.kr/stations/{station_id}/?sy={year}&ey={year}&format=csv"
    with open(filename, "w", encoding="UTF-8-sig") as f:
        resp = requests.get(URL)
        resp.encoding = "UTF-8"
        f.write(resp.text)

def main():
    name = "민시윤"
    affiliation = "스마트팜학과"
    student_id = "202420947"

    # 1번
    filename = "weather_146_2012.csv"
    download_weather(146, 2012, filename)
    df = pd.read_csv(filename, skipinitialspace=True)
    answer1 = round(df["rainfall"].sum(), 1)
    print(answer1)

    # 2번
    filename = "weather_146_2024.csv"
    download_weather(146, 2024, filename)
    df = pd.read_csv(filename, skipinitialspace=True)
    answer2 = round(df["tmax"].max(), 1)
    print(answer2)

    # 3번
    filename = "weather_146_2020.csv"
    download_weather(146, 2020, filename)
    df = pd.read_csv(filename, skipinitialspace=True)
    df["tdiff"] = df["tmax"] - df["tmin"]
    answer3 = round(df["tdiff"].max(), 1)
    print(answer3)

    # 4번
    filename1 = "weather_119_2019.csv"
    download_weather(119, 2019, filename1)
    df1 = pd.read_csv(filename1, skipinitialspace=True)

    filename2 = "weather_146_2019.csv"
    download_weather(146, 2019, filename2)
    df2 = pd.read_csv(filename2, skipinitialspace=True)

    diff = abs(df1["rainfall"].sum() - df2["rainfall"].sum())
    answer4 = round(diff, 1)
    print(answer4)

    
    submit_to_api(name, affiliation, student_id, answer1, answer2, answer3, answer4, verbose=True)

if __name__ == "__main__":
    main()
