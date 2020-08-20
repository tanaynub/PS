x = int(input(''))
for i in range(x):
    inp = input('')
    if (len(inp) <= 10):
        print(inp)
    else:
        c = len(inp) - 2
        print(f"{inp[0]}{c}{inp[-1]}")