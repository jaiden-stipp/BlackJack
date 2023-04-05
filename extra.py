class Solution(object):
    def __init__(self):
        self.answer = []
    def twoSum(self, nums, target, pointer = 0, pointerp = 1):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if pointer > len(nums) - 1:
            pass

        elif pointerp > len(nums)-1:
            self.twoSum(nums, target, pointer + 1, pointerp = 0)
        elif pointer == pointerp:
            self.twoSum(nums, target, pointer, pointerp + 1) 
        elif nums[pointer] + nums[pointerp] == target:
            print(pointer, pointerp)
            self.answer.append(pointer)
            self.answer.append(pointerp)
            return self.answer
        elif pointerp <= len(nums)-1:
            self.twoSum(nums, target, pointer, pointerp + 1)
        
        return self.answer

test = Solution()
nums = [3, 2, 4]
target = 6
print(test.twoSum(nums, target))