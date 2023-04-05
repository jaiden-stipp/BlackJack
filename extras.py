class Solution(object):
    def __init__(self):
        self.answer = []
    def twoSum(self, nums, target):
        for pointer in range(len(nums)):
            for i in range(len(nums)):
                if pointer == i:
                    continue
                elif nums[pointer] + nums[i] == target:
                    self.answer.append(pointer)
                    self.answer.append(i)
                    return self.answer
test = Solution()
nums = [3, 2, 4]
target = 6
print(test.twoSum(nums, target))