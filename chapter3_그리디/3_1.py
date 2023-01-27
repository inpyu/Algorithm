n = 1260

money_list = [500,100,50,10]
count = 0

for i in money_list:
    count += int(n / i)
    n = n-i*int(n/i)

print(count)