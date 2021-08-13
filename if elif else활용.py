"""
복싱 체급 계산기 프로그램
몸무게를 입력받아 체급을 출력하는 프로그램
몸무게가 50.8kg 이하 - Flyweight
61.23kg 이하 - Lightweight
72.57kg 이하 - Middleweight
88.45kg 이하 - Cruiserweight
그 이상은 Heavyweight
"""
print("복싱 체급안내 하겠습니다")
print("===================================================")

weight = float(input("몸무게가 몇인가요? 소수점 2자리까지 입력하세요"))

if weight < 0 :
  print("잘못 입력하였습니다")
  exit()

if 50.8 >= weight :
  print("Flyweight 입니다")
elif 61.23 >= weight :
  print("Lightweight 입니다")
elif 72.57 >= weight :
  print("Middleweight 입니다")
elif 88.45 >= weight :
  print("Cruiserweight 입니다")
else :
  print("Heavyweight 입니다")













