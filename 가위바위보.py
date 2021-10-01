import random

print("가위바위보를 시작합니다")

while True :
    computer = random.choice(["가위","바위","보"])
    player = input("무엇을 내겠습니까 : ")
    
    if computer == "가위":
        print("computer = 가위")
        if player == "가위" :
            print("비겼다")
        elif player == "바위":
            print("이겼다")
        elif player =='보':
            print("졌다")
            
    elif computer == "바위" :
        print("computer = 바위")
        if player == "바위" :
            print("비겼다")
        elif player == "보":
            print("이겼다")
        elif player == '가위':
            print("졌다")
            
    elif computer == "보" :
        print("computer = 보")
        if player == "보" :
            print("비겼다")
        elif player == "가위":
            print("이겼다")
        elif player =='주먹':
            print("졌다")
            
    q = input("더 할거야? Y/N")
    if q == "Y" or q == "y" :
        continue
    elif q == "N" or q == "n" :
        print("프로그램 종료")
        break
        








        
