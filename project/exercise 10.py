import fractions
def lcm(n):
    ans = 1
    for i in range(1, n + 1):
        ans = (ans * i)/fractions.gcd(ans, i)
n=5
print(lcm(n))
