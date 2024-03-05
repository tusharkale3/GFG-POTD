Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#User function Template for python3

class Solution:
    def maxIndexDiff(self, a, n):
        diff = 0
        count = 0
        for i in range(n):
            for j in range(n-1, i-1, -1):
                if a[j] >= a[i]:
                    count = j - i
                    diff = max(diff, count)
                    break
        return diff



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            ob=Solution()
            print(ob.maxIndexDiff(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends