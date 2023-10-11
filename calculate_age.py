from datetime import date

def calculate_age(birth_year, birth_month, birth_day):
    # 현재 날짜 구하기
    today = date.today()
    
    # 생년월일을 사용하여 나이 계산
    age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_day))
    
    return age

# 생년월일 입력 (예: 2000년 1월 1일)
birth_year = int(input("태어난 년도를 입력하세요: "))
birth_month = int(input("태어난 월을 입력하세요: "))
birth_day = int(input("태어난 일을 입력하세요: "))

# 나이 계산 함수 호출
age = calculate_age(birth_year, birth_month, birth_day)

# 결과 출력
print(f"만 나이는 {age}세 입니다.")
