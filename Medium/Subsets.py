import copy

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        retSet = self.helper(nums, [], set())
        retSet.add(str(nums))
        retArr = []
        for elem in retSet:
            retArr.append(elem.strip('][').split(', '))
        return retArr
            
        
    def helper(self, nums, curArr, retArr):
        if not nums:
            return retArr
        temp = copy.deepcopy(nums)
        for i in range(len(nums)):
            valToDelete = temp[i]
            del temp[i]
            retArr.add(str(temp))
            self.helper(temp, curArr, retArr)
            temp.insert(i, valToDelete)
            
        return retArr
            