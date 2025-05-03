import os
import requests

def download_weather_2020(filename):
    if not os.path.exists(filename):
        URL = "https://api.taegon.kr/stations/146/?sy=2020&ey=2020&format=csv"
        resp = requests.get(URL)
        resp.encoding = "UTF-8"
        with open(filename, "w", encoding="UTF-8-sig") as f:
            f.write(resp.text)

def analyze_weather(filename, result_file):
    with open(filename, encoding="UTF-8-sig") as f:
        lines = f.readlines()

    total_temp = 0
    temp_count = 0
    rain_days = 0
    total_rain = 0

    for line in lines[1:]:
        tokens = line.strip().split(",")
        try:
            avg_temp = float(tokens[4])
            rainfall = float(tokens[6])

            if avg_temp != -99:
                total_temp += avg_temp
                temp_count += 1

            if rainfall >= 5:
                rain_days += 1

            if rainfall != -99:
                total_rain += rainfall
        except:
            continue

    avg_temp_result = total_temp / temp_count if temp_count > 0 else 0

    with open(result_file, "w", encoding="UTF-8-sig") as fout:
        fout.write("2020년 연평균 기온: {:.2f}℃\n".format(avg_temp_result))
        fout.write("5mm 이상 강우일수: {}일\n".format(rain_days))
        fout.write("총 강우량: {:.1f}mm\n".format(total_rain))

def main():
    filename = "hw12/weather_146_2020.csv"
    result_file = "hw12/weather_result_2020.txt"

    download_weather_2020(filename)
    analyze_weather(filename, result_file)

if __name__ == "__main__":
    main()