class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        zeroCount = 0
        zeroLocation = []
        product = 1

        for n in nums:
            if n == 0:
                continue
            product *= n
        
        for i, n in enumerate(nums):
            try:
                output.append(product//n)
            except ZeroDivisionError:
                zeroCount +=1
                zeroLocation.append(i)
                output.append('p')
        
        match zeroCount:
            case 0:
                return output
            case 1:
                output = [0]*len(nums)
                output[zeroLocation[0]] = product
                return output
            case _:
                return [0]*len(nums)
                
        