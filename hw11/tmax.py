def calculate_accumulated_temperature(dates, tmax):
    accum_temp = {}

    for i in range(len(dates)):
        year, month, day = dates[i]
        if 5 <= month <= 9:
            if year not in accum_temp:
                accum_temp[year] = 0
            accum_temp[year] += tmax[i]

    print("2. 연도별 5~9월 적산온도:")
    for year in sorted(accum_temp.keys()):
        print(f"{year} {accum_temp[year]:.1f}")


def main():
    filename = "hw11/weather(146)_2001-2022.csv"

    with open(filename) as f:
        lines = f.readlines()

    dates = []
    tmax = []

    for line in lines[1:]:
        tokens = line.strip().split(",")
        dates.append([int(tokens[0]), int(tokens[1]), int(tokens[2])])
        tmax.append(float(tokens[3]))

    calculate_accumulated_temperature(dates, tmax)


if __name__ == "__main__":
    main()
