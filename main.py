class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        largeInteger = int(''.join(map(str, digits)))
        largeInteger_str= str(largeInteger + 1)
        return [int(char) for char in largeInteger_str]
        
