import requests


# 요청 URL
url = "http://apis.data.go.kr/B552061/AccidentDeath/getRestTrafficAccidentDeath"

# 요청에 필요한 매개변수
params = {
    'ServiceKey': f"write your service api key",  # 여기서 '인증키'를 실제 API 키로 바꿔주세요
    'searchYear': 2022,
    'siDo': 1100,
    'guGun': 1116,
    'numOfRows': 20,
    'pageNo': 1
}

year = [
    2021,
    2022,
    2023
]

seoul_guGun_request_val_list = [
1116,
1117,
1124,
1111,
1115,
1123,
1112,
1125,
1122,
1107,
1105,
1114,
1110,
1109,
1119,
1104,
1106,
1118,
1120,
1113,
1103,
1108,
1101,
1102,
1121
]