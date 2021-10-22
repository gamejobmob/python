리스트 = ["dog", "cat", "parrot"]
for w in 리스트:
     f = w[0]
     f2 = f.upper()
     print(f2 + w[1:])


print("=" * 30)



for g in range(2,10):
    for s in range(1,10):
        print("%d * %d = %d" %(g, s, g * s))
         
