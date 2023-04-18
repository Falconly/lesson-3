number = int(input())


for divider in range(2, number // 2 + 1):
    if number % divider == 0:
        print('Составное')
        break
else:
    print('Простое')
