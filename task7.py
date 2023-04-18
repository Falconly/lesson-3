n = int(input())

# Отсчет с 1

start = [1, 1]

for i in range(1, n - 1):
    start.append((start[-1] + start[-2]))

print(start[-1])
