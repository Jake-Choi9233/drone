import requests

url = "http://116.62.112.202:5000/upload"  # 서버 주소
data = {'value': '9233'}  # 여기에 원하는 숫자 입력

response = requests.post(url, data=data)

print("응답 코드:", response.status_code)
print("응답 내용:", response.text)