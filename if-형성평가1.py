"""
2개의 수를 입력받아 큰 수와 작은수의 차를 출력하는 프로그램
"""
num1 = int(input("1번째수"))
num2 = int(input("2번째수"))

if num1 > num2 :
  result = num1 - num2
else :
  result = num2 - num1

print("result = %d" %(result))

result = num1 - num2 if num1 > num2 else num2 - num1

print("result = %d" %(result))

