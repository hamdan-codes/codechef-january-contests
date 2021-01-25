# Contributor Chaudhary Hamdan

t = int(input())
for _ in range(t):
    n,k,d = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    total = sum(a)
    ans = total // k
    if ans > d:
        ans = d
    print(ans)