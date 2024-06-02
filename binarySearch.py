'''
Finds an item in the sorted list in O(logn) time.

* Start with the middle number, if middle number is the target, then return it
* Compare target with the middle number and decide if you'll search the target in 
left or right sub arrays
* Then repeat the same steps on the new half-size problem
'''


# Iterative implementation

class Solution:

    def binarySearch(nums, target):

        leftBoundry = 0
        rightBoundry = len(nums) - 1

        while leftBoundry <= rightBoundry:
            distance = rightBoundry + leftBoundry
            middleIndex = distance // 2

            middleNum = nums[middleIndex]

            if middleNum == target:
                return True

            if middleNum > target:
                rightBoundry = middleIndex - 1

            else:
                leftBoundry = middleIndex + 1

        return False


# test case
nums = [1, 2, 3, 4, 5, 6, 7, 8]
target = 10
answer = Solution.binarySearch(nums, target)
print(answer)
