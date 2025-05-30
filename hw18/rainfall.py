import requests
import pandas as pd


def download_weather(station_id, year, filename):
    URL = f"https://api.taegon.kr/stations/{station_id}/?sy={year}&ey={year}&format=csv"
    with open(filename, "w", encoding="UTF-8-sig") as f:
        resp = requests.get(URL)
        resp.encoding = "UTF-8"
        f.write(resp.text)




def main():
    filename="weather_146_2012.csv"
    download_weather(146,2012,"weather_146_2012.csv")
    df=pd.read_csv(filename,skipinitialspace=True)
    print(round(df["rainfall"].sum(), 1))

    filename="weather_146_2024.csv"
    download_weather(146,2024,"weather_146_2024.csv")
    df=pd.read_csv(filename,skipinitialspace=True)
    print(round(df["tmax"].max(),1))

    filename="weather_146_2020.csv"
    download_weather(146,2020,"weather_146_2020.csv")
    df=pd.read_csv(filename,skipinitialspace=True)
    df["tdiff"]=df["tmax"]-df["tmin"]
    print(round(df["tdiff"].max(),1))
    
    filename1 = "weather_119_2019.csv"
    download_weather(119, 2019, filename1)
    df1 = pd.read_csv(filename1, skipinitialspace=True)

    filename2 = "weather_146_2019.csv"
    download_weather(146, 2019, filename2)
    df2 = pd.read_csv(filename2, skipinitialspace=True)

    print(round(abs(df1["rainfall"].sum() - df2["rainfall"].sum()), 1))


    
    

if __name__ == "__main__":
    main()