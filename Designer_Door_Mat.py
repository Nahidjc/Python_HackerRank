N,M=map(int,input().split())
s1='.|.'
s2='WELCOME'
for n in range(N//2):
    print((s1*((n*2)+1)).center(M,'-'))
print(s2.center(M,'-'))
for n in range(N//2-1,-1,-1):
    print((s1*((n*2)+1)).center(M,'-'))