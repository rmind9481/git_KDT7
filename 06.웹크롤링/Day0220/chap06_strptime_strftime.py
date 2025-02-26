import datetime

# 원래 문자열에서 탭 문자 제거 및 쉼표 뒤 공백 추가
date_string = "Tue, 13 Aug 2024 09:02:00 +0900"

# datetime 형식으로 변환
pdate = datetime.datetime.strptime(date_string, '%a, %d %b %Y %H:%M:%S %z')

print(type(pdate))

# strftime(format): datetime -> string 변환
pdate_string = pdate.strftime('%Y-%m-%d %H:%M:%S')
print(type(pdate_string))
print(pdate_string)


