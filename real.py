class Solution:
    def twoSum(self, nums: int, target: int):
        if target == 0: return [[]]
        if target <0 or nums==[]: return None
        
        sum = []
        for index, i in enumerate(nums):
            li = nums.copy()
            li.pop(index)
            print(li)
            s = self.twoSum(li, target-i)
            if s != None:
                s.append(i)
                sum=s
        return sum

d = Solution()
print(d.twoSum([34,3], 6))