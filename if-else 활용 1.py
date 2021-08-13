"""
나이를 입력받아 20세 이상이면 An adult
그렇지 않으면 몇년 이후에 성인이 되는지  () years 라는 메세지를 출력하기
"""

age = int(input("나이 몇임?"))

if age >= 20 :
  print("An adult")

else :
  print("%d years" %(20 - age))
