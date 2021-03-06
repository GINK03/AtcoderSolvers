
# floor(N/m) = N%m 
# これは、 N = k*m + k -> N = k(m+1)
# となり約数の問題にすることができる
N=int(input())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

divs = make_divisors(N)
acc = 0
for div in divs:
    if div > 1 and N//(div-1)==N%(div-1):
        acc+=div-1
print(acc)

