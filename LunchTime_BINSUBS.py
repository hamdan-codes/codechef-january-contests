# Contributor Chaudhary Hamdan

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    ans = 0
    o = s.count('1')
    ans = o
    for i in range(n):
        if s[i] == '0':
            o += 1
        else:
            o -= 1
        if o > ans:
            ans = o
    print(n-ans)
    
    



