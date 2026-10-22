class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_product = 1
        num_product_zero = 1
        zero_count = 0

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                num_product *= num

        output = []
        for num in nums:
            result = 1
            if zero_count:
                if num == 0 and zero_count == 1:
                    result *= num_product // 1
                else:
                    result *= 0
            else:
                result *= num_product // num
            
            output.append(result)
        
        return output


            
