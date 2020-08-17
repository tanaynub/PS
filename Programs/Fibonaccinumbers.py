
# def even_fibonacci_sum(n):
#     n1 = 1 #Fn-2
#     n2 = 1 #Fn-1
#     sum = 0
#     while True :
#         t = n1 + n2 
#         if t >= n: return sum
#         if t % 2 == 0: sum += t
#         n2= n1
#         n1 = t



a = int(input(""))
b = int(input(""))
c = int(input(""))

if a > b:
    if a > c:
        print(f"{a} is the greatest")
if b > a:
    if b>c:
        print(f"{b} is the greatest")
if c>a :
    if c>b:
        print(f"{c} is the greatest")