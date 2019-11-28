prices = [10,50,100,40,-50,-100]
sum=0
for i in prices:
    sum+=i
    if i<0:
        break
    print(sum)