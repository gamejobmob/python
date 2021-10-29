def star(a):
    print("별 출력중...")
    for i in range(a):
        for j in range(i+1):
            print("*", end='')
        print()

print(star(10))

