n, m = map(int, input().split())

data_set = []

for i in range(0,n):
    data = list(map(int, input().split()))
    data_set.append(min(data))
    data.clear()

print(max(data_set))