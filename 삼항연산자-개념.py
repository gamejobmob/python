"""
삼항연산자.py
if (a
else

삼항연산자를 이용하여 두 수중 가장 작은값 출력
"""
num1 = int(input("1번째 수"))
num2 = int(input("2번째 수"))

min_data = num2 if num1 > num2 else num1

print("min_data = %d" %(min_data))
