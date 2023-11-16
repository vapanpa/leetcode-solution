class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        check = {}
        for i in nums:
            if i not in check:
                check[i] = 1
            else:
                check[i] = check[i] + 1

        for i in check:
            if check[i] == 1:
                return i
