n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True) #입력받은 수 정렬하기

result = 0
count =0
for i in range(0,m):
    if(count == k):
        result += data[1]
        count = 0
    else:
        result += data[0]
        count +=1

print(result)