import random
import time

words = ["그누구보다빠르게난남들과는다르게", "췍췍 암더코리안탑클래스히합모범노블레스", "하이브리드샘이솟아리오레이비", "정신차려이각박한세상속에서", "꿻뚨훯렗", "월우럴우얼월월월!!", "봟꿟쐃귏궚"]


n = 1

print("준비되면 엔터")
input()
start = time.time()
q = random.choice(words)

while n <= 5 :
    print("문제:", n)
    print(q)
    x = input()
    if q == x:
        print("통과")
        n += 1
        q = random.choice(words)
    else :
        print("오타입니다")
              
end = time.time()
et = end - start
et = format(et, "2f")
print("총 걸린시간 :", et, "초")

