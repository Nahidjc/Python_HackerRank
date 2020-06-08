def print_rangoli(size):
    l=list(map(chr,range(97,123)))
    x = l[n-1::-1]+l[1:n]
    m=len('-'.join(x))
    for i in range(1,n):
        print(('-'.join(l[n-1:n-i:-1]+l[n-i:n])).center(m,'-'))
    print('-'.join(x))
    #print(('-'.join(x)).center(m,'-'))
    for i in range(n-1,0,-1):
        print(('-'.join(l[n-1:n-i:-1]+l[n-i:n])).center(m,'-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)