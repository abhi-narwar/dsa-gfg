class Solution:
    def getSecondLargest(self, arr):
        first = second = float('-inf')
        
        for num in arr:
            if num > first:
                second = first
                first = num
            elif num > second and num != first:
                second = num
        
        if second == float('-inf'):
            return -1
        else:
            return second
s=Solution()
print(s.getSecondLargest([9,9,9,9,9,9]))
print(s.getSecondLargest([9,7,5,4,3,2,1]))
