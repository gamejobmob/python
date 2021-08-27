"""
주사위 2번 던져서 나온 수를 입력받아 두 수가 모두 4 이상이면 이.겼습니다 한개만 4 이상이면 비겻습니다
모두 4 미만이면 졌습니다 라고 출력하기
"""

num1 = int(input("1번째 값은?"))

num2 = int(input("2번째 값은?"))

if num1 > 6 or num2 > 6 or num1 < 1 or num2 < 1 :
  print("잘못 입력하셨습니다")
  exit()
  
if num1 >= 4 and num2 >= 4 :
  print("이겼습니다")
elif num1 <= 4 or num2 <= 4 :
  print("비겼습니다")
else :
  print("졌습니다")
  





























