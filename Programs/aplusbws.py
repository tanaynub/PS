# this program solves a+b whole square

def asqplusbsq(a,b):
    ans = a**2 + b**2 + 2*a*b
    return ans

x = int(input('Enter the value of A: '))
y = int(input('Enter the value of B: '))


print(f"the answer is {asqplusbsq(x,y)}")