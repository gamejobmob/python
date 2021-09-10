import random


num1 = int(input("복권1"))
num2 = int(input("복권2"))
num3 = int(input("복권3"))
num4 = int(input("복권4"))
num5 = int(input("복권5"))
num6 = int(input("복권6"))

if 20 < num1 or 20 < num2 or 20 < num3 or 20 < num4 or 20 < num5 or num6 > 20 :
           print("1부터 20 사이의 숫자로만 정해주세요")
           exit()
elif 1 > num1 or  1 > num2 or 1 > num3 or 1 > num4 or 1 > num5 or num6 < 1 :
  print("1부터 20 사이의 숫자로만 정해주세요")
  exit()
  
print("%d,%d,%d,%d,%d,%d" %(num1,num2,num3,num4,num5,num6))

num7 = random.randrange(1,21)
num8 = random.randrange(1,21)
num9 = random.randrange(1,21)
num10 = random.randrange(1,21)
num11 = random.randrange(1,21)
num12 = random.randrange(1,21)

if num1 == num7 :
    prize = 1
else :
    prize = 0
if num2 == num8 :
    prize = prize + 1
if num3 == num9 :
    prize = prize + 1
if num4 == num10 :
    prize = prize +1
if num5 == num11 :
    prize = prize +1
if num6 == num12 :
    prize = prize +1

final = prize * 5000 * prize
print("당신의 당첨금은...")
print("%d 원 !" %(final))






