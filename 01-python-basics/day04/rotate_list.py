nums=[1,2,3,4,5]
k=2
k=k%len(nums)
rotate=nums[-k:]+nums[:-k]
print(rotate)