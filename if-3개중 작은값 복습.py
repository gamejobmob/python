num1 = int(input("1번째 수는?"))
num2 = int(input("2번째 수는?"))
num3 = int(input("3번째 수는?"))

if num1 < num2 :
  min_data = num1
  if min_data > num3 :
    min_data = num3

else :
  min_data = num2
  if min_data < num3 :
    min_data = min_data
  else:
      min_data = num3

print("min_data = %d" %(min_data))


  


