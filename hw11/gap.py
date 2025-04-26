def find_max_gap_each_year(dates, tmax, tmin):
    year_max_gap = {}
    year_max_date = {}

    for i in range(len(dates)):
        year = dates[i][0]
        gap = tmax[i] - tmin[i]

        if year not in year_max_gap or gap > year_max_gap[year]:
            year_max_gap[year] = gap
            year_max_date[year] = dates[i]

    print("1. 연도별 최대 일교차 일자와 일교차:")
    for year in sorted(year_max_date.keys()):
        date = year_max_date[year]
        gap = year_max_gap[year]
        print(f"{date[0]}/{date[1]:02}/{date[2]:02} {gap:.1f}")


def main():
    filename = "hw11/weather(146)_2001-2022.csv"

    with open(filename) as f:
        lines = f.readlines()

    dates = []
    tmax = []
    tmin = []

    for line in lines[1:]:
        tokens = line.strip().split(",")
        dates.append([int(tokens[0]), int(tokens[1]), int(tokens[2])])
        tmax.append(float(tokens[3]))
        tmin.append(float(tokens[5]))

    find_max_gap_each_year(dates, tmax, tmin)


if __name__ == "__main__":
    main()