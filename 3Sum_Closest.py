class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        
        closest = float('inf')  

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

               
                if abs(target - total) < abs(target - closest):
                    closest = total

                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total  

        return closest