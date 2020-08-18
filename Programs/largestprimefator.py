num = int(input("enter a number: "))
for i in range (1,num+1):
    if num % i == 0:
        # print(i)
        for j in range(2, i):
            if i%j != 0:
                continue
            if i%j == 