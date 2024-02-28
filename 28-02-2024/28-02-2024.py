Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#User function Template for python3



class Solution:
    def DivisibleByEight(self,s):
        # Check if the length of the string is less than 3
        if len(s) < 3:
            num = int(s)
        else:
            # Extract the last three digits
            num = int(s[-3:])
        
        # Check if the last three digits are divisible by 8
        if num % 8 == 0:
            return 1
        else:
            return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        S=input()
        ob=Solution()
        print(ob.DivisibleByEight(S))
# } Driver Code Ends