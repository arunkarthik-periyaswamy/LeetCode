class Solution:
    # def isPalindrome(self, x: int) -> bool:
    #     if x > 0:
    #         # continue
    #         # i=for i in list(x)
    #         lst= []
    #         while x // 10 != 0:
    #             val = x % 10
    #             lst.append(val)
    #             val2 = x // 10
    #             # if val2 = 0:
    #             #     break 
    #             x = val2
    #         lst.append(x)
    #         for i in range(round(len(lst)/2)):
    #             negative_v = i+1
    #             if  lst[i] == lst[-negative_v]:
    #                 return True
    #             else:
    #                 return False
    #         print(list(x)) 
    #     else:
    #         return False
     def isPalindrome(self, x: int) -> bool:
        if x < 0:  # Check for negative numbers
            return False

        # Initialize variables for reversing the number
        reversed_num = 0
        original_num = x

        # Reverse the second half of the number and compare with the first half
        while x != 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10

        return original_num == reversed_num     