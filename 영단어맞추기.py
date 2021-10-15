print("=" * 30)
print("영어단어 맞추기 게임")
print("=" * 30)

dic = {
    "grape" : "포도",
    "curry" : "카레",
    "airplane" : "비행기",
    "zoo" :"동물원",
    "sun" : "태양",}

for word in dic.keys():
    korean = dic[word]
    guess = input("{}단어를 번역하세요".format(word))

    if guess == korean:
        print("정답")
    else :
        print("오답")

print("프로그램 종료")





    
