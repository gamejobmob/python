"""
if-형성평가2.py

정수를 이어받아 0이면 zero
양수이면 plus
음수이면 minus
출력하는 프로그램
"""
num1 = int(input("정수를 입력하세요"))

if num1 > 0 :
 print("plus")
elif num1 == 0 :
 print("zero")
else :
  print("minus")

