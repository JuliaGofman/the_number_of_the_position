lst = [int(i) for i in input().split()]
g = int(input())
if g not in lst:
    print('Отсутствует')
else:
    for a in lst:
        if lst.count(g) >= 1:
            a = lst.index(g)
            print(a, end=' ')
            lst[0:a+1] = [0] * (a+1)