def fac(a):
    if a <= 1:
        return 1
    return a * fac(a-1)

n = int(input())
print(fac(n))
