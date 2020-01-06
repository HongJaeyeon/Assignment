import time

# 재귀적 구현
def iterfibo(n) :
    if n == 0 :
        return 0
    elif n == 1:
        return 1
    else :
        return iterfibo(n-1) + iterfibo(n-2)

# 반복적 구현
def fibo(num):
    f = []
    for num in range(nbr+1):
        if (num == 0): f.append(0)
        elif (num==1): f.append(1)
        else:f.append(f[num-1]+f[num-2])

    return f[num]

# 입출력
try:
    while True:
        nbr = int(input("Enter a number: "))
        if nbr == -1:
            break
        ts = time.time()
        fibonumber = iterfibo(nbr)
        ts = time.time() - ts
        print("IterFibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))
        ts = time.time()
        fibonumber = fibo(nbr)
        ts = time.time() - ts
        print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber, ts))

except ValueError:
print("ValueError")
