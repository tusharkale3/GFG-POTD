Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#User function Template for python3

class Solution:
    
    def count(self, n):
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(3, n+1):
            dp[i] += dp[i-3]
        for i in range(5, n+1):
            dp[i] += dp[i-5]
        for i in range(10, n+1):
            dp[i] += dp[i-10]
        return dp[n]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        ob = Solution()
        print(ob.count(n))
        
# } Driver Code Ends