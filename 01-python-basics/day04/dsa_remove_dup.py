def remove_dup(nums):
    if len(nums)==0:
        return 0
    j=0
    for i in range(1,len(nums)):
        if nums[i] !=nums[j]:
            j+=1
            nums[j]=nums[i]
    return j+1
nums=[0,0,1,1,1,2,2,3,3,4,4]
length = remove_dup(nums)

print(nums[:length])