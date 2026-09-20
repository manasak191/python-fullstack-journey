nums=[1,2,3,4]
result=[]
sum=0
for num in nums:
    if num not in result:
        sum +=num
        result.append(sum)
print(result)