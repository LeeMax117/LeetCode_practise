class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_letter_dict = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        output = []
        for num in digits:
            lst = num_letter_dict[num]
            if len(output) == 0:
                output = [x for x in lst]
            else:
                output = [output_letter + letter for letter in lst for output_letter in output]
        return output
