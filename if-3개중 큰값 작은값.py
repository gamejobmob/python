"""
정수 3개를 입력받아 그중 가장큰수와 작은수를 출력하는 프로그램
max_data : 가장 큰 수
min_data : 가장 작은수
num1 num2 num3
"""
num1 = int(input("1번째 수는"))
num2 = int(input("2번째 수는"))
num3 = int(input("3번째 수는"))

if num1 > num2 :
  max_data = num1
  min_data = num2
else :
  max_data = num2
  max_data = num1

if max_data < num3 :
  max_data = num3
else :
  if min_data > num3 :
    num3 = min_data


print("max_data = %d" %(max_data))

print("min_data = %d" %(min_data))










