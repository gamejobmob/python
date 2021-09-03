"""
삼항연산자를 이용하여 세 수중 가장 작은값 출력
"""
num1 = int(input("1번째 수"))
num2 = int(input("2번째 수"))
num3 = int(input("3번째 수"))

min_data = num2 if num1 > num2 else num1
min_data = num3 if min_data > num3 else min_data

print("min_data = %d" %(min_data))
