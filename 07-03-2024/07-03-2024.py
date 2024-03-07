Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#User function Template for python3

class Solution:
    def longestSubstring(self, s, n):
        # Initialize a 2D table to store the lengths of longest common suffixes
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        # To store length of the longest repeating non-overlapping substring
        max_length = 0
        
        # To store the index where the longest repeating substring starts
        max_index = 0
        
        # Traverse the string and fill the dp table
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                if s[i - 1] == s[j - 1] and dp[i - 1][j - 1] < (j - i):
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > max_length:
                        max_length = dp[i][j]
                        max_index = max(i, max_index)
                else:
                    dp[i][j] = 0
        
        # If no repeating non-overlapping substring found
        if max_length == 0:
            return "-1"
        
        # Return the substring using the max_index
        return s[max_index - max_length:max_index]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        S=input()
        
        ob = Solution()
        print(ob.longestSubstring(S , N))
# } Driver Code Ends