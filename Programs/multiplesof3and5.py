a = int(input('enter a number: '))
sum = 0
for i in range(a):
    if i%3==0 or i%5==0:
      sum+=i
print(sum)