def read_db(filename):
    temperatures=[]
    rain_amounts=[]

    with open(filename, encoding="utf-8-sig") as f:        
        lines = f.readlines()                              
        #print(lines) 
        for line in lines[1:]:                   
            line = line.strip()                        
            tokens = line.split(",")                     
            tavg = float(tokens[4])                       
            rainfall = float(tokens[9]) 
            temperatures.append(tavg) 
            rain_amounts.append(rainfall)
            #print(line)

    return temperatures, rain_amounts


def main():
    tavg, rainfall = read_db("./weather(146)_2022-2022.csv")
    avg_temp = sum(tavg) / len(tavg)
    over_5mm_days = sum(1 for r in rainfall if r >= 5.0) 
    total_rain = sum(rainfall)

    print(f"연 평균 기온: {avg_temp:.1f}℃")
    print(f"5mm 이상 강우일 수: {over_5mm_days}일")
    print(f"총 강우량: {total_rain:.1f}mm")

if __name__ == "__main__":
    main()
