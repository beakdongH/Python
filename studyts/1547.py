n = int(input())
nums=[0,1,2,3]

for i in range(n):
    ch1, ch2=map(int,input().split())
    nums[ch1],nums[ch2] = nums[ch2],nums[ch1]

print(nums.index(1))