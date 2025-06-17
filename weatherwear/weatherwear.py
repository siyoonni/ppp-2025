import PySimpleGUI as sg

def recommend_outfit(temp, weather, cold_sensitive, heat_sensitive):
    temp = int(temp)

    # 상의/하의 추천
    if temp >= 27:
        top = "나시, 반팔"
        bottom = "반바지, 얇은 긴바지"
    elif 23 <= temp <= 26:
        top = "반팔, 린넨셔츠, 얇은 긴팔"
        bottom = "반바지, 얇은 긴바지"
    elif 20 <= temp <= 22:
        top = "얇은 맨투맨, 얇은 후드티, 셔츠, 얇은 가디건"
        bottom = "긴바지"
    elif 17 <= temp <= 19:
        top = "니트, 가디건, 후드티, 맨투맨, 자켓"
        bottom = "긴바지"
    elif 12 <= temp <= 16:
        top = "맨투맨, 후드티, 니트, 자켓, 청자켓"
        bottom = "긴바지"
    elif 9 <= temp <= 11:
        top = "트렌치코트, 항공점퍼, 기모맨투맨, 기모후드티"
        bottom = "긴바지"
    elif 5 <= temp <= 8:
        top = "코트, 무스탕, 가죽자켓, 기모 후드티, 기모 맨투맨, 니트"
        bottom = "긴바지"
    else:
        top = "패딩, 코트, 기모 후드티, 기모 맨투맨, 니트"
        bottom = "긴바지"

    # 신발 추천
    if weather == "맑음" or weather == "흐림":
        shoes = "운동화, 캐쥬얼 슈즈"
    elif weather == "비":
        shoes = "운동화, 레인부츠, 캐쥬얼 슈즈"
    elif weather == "눈":
        shoes = "(미끄럽지 않은) 운동화, 캐쥬얼 슈즈"

    # 조언
    advice = ""
    if cold_sensitive == "예":
        if temp >= 27:
            advice += "에어컨 바람에 대비해 얇은 겉옷 챙기기!\n"
        elif temp <= 8:
            advice += "히트텍 필수!\n"
    if heat_sensitive == "예":
        if 20 <= temp <= 22:
            advice += "반팔도 추천!\n"

    return top, bottom, shoes, advice

# GUI 구성
layout = [
    [sg.Text("오늘 기온을 입력하세요 (숫자만, °C):")],
    [sg.Input(key="TEMP")],
    [sg.Text("오늘 날씨를 선택하세요:")],
    [sg.Combo(["맑음", "흐림", "비", "눈"], key="WEATHER")],
    [sg.Text("추위를 많이 타시나요?")],
    [sg.Combo(["예", "아니오"], key="COLD")],
    [sg.Text("더위를 많이 타시나요?")],
    [sg.Combo(["예", "아니오"], key="HEAT")],
    [sg.Button("추천받기"), sg.Button("종료")]
]

window = sg.Window("WeatherWear", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "종료":
        break

    if event == "추천받기":
        try:
            temp = int(values["TEMP"])
            weather = values["WEATHER"]
            cold = values["COLD"]
            heat = values["HEAT"]

            if not weather or not cold or not heat:
                sg.popup("모든 항목을 선택해주세요.")
                continue

            top, bottom, shoes, advice = recommend_outfit(temp, weather, cold, heat)

            result = f"WeatherWear 추천\n"
            result += f"- 상의: {top}\n"
            result += f"- 하의: {bottom}\n"
            result += f"- 신발: {shoes}\n"
            if advice:
                result += f"- 조언: {advice}"

            sg.popup(result)

        except ValueError:
            sg.popup("기온은 숫자로 입력해주세요.")

window.close()
