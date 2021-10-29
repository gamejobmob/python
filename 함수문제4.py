kor, eng, mat = map(int,input("과목의 점수를 입력하세요").split())
def average(kor, eng, mat):
    hap = kor + eng + mat
    fin = hap/3
    return fin
print("국어, 영어, 수학의 점수 =", kor, eng, mat)

avg = average(kor, eng, mat)

print("평균 = %.2f"%avg)

