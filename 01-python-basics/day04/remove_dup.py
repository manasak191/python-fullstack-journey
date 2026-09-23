nums=[2,4,3,1,3,4,2,5,2,1,3,6,9,12,50,34]
# dup=set(num)
# print(dup)
    #or
    
# unique=list(set(nums))
# print(sorted(unique))
    # or 
    
     
#seen=[]
#for num in nums:
 #   if num not in seen:
  #      seen.append(num)
#print(seen)


#or 

seen = set()
unique = []
for num in nums:
    if num not in seen:
        unique.append(num)
        seen.add(num)
print(unique)