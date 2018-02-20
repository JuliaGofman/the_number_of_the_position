lst = [int(i) for i in input().split()]
g = int(input())
if g not in lst:
    print('Отсутствует')
for i in range(len(lst)):
    if lst[i] == g:
        print(i, end=' ')