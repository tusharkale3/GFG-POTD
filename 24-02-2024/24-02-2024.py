Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Solution:
    def maxSum(self, n):
        memo = {}

        def helper(num):
            if num <= 0:
                return 0
            
            if num in memo:
                return memo[num]
            
            max_sum = max(num, helper(num // 2) + helper(num // 3) + helper(num // 4))
            
            memo[num] = max_sum
            
            return max_sum
        
        return helper(n)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.maxSum(n))
