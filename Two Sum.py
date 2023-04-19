class Solution(object):
    def twoSum(self, nums, target):
        for number in range(len(nums)):
            for i in range(0, len(nums)):
                if number != i:
                    if nums[number] != nums[i]:
                        if nums[number] + nums[i] == target:
                            return [number, i]
                        else:
                            pass
                    elif nums[number] == nums[i]:
                        if nums[number] + nums[i] == target:
                            return [number, i]
                        else:
                            pass
                elif len(nums) <= 2:
                    return [number, i+1]
