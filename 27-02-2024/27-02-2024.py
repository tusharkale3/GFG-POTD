Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#User function Template for python3

class Solution:
    def game_with_number(self, arr, n):
        for i in range(n-1):
            arr[i] |= arr[i+1]
        return arr

#{ 
 # Driver Code Starts

#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    res = ob.game_with_number(arr, n);
    print(*res)




# } Driver Code Ends