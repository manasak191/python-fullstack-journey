nums=[2,5,8,9,3,12,7]
# nums.sort()
#second_num=nums[-2]
#print(second_num)
     # or

largest=0

for num in nums:
    if num>largest:
        second=largest
        largest=num
    elif num>second:
        second=num
print(second)        
        