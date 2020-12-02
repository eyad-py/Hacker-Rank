if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lis=list(arr)
    m1=max(lis)
    m2 = -99999999999999999999999999999
    for i in range(n):
        if lis[i] != m1 and lis[i] > m2:
            m2 = lis[i]
    print(m2)
