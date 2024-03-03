Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#User function Template for python3
class Solution:

    def printLargest(self, n, arr):
        # Define custom comparison function for sorting
        def compare(a, b):
            # Concatenate a and b in different orders
            order1 = a + b
            order2 = b + a
            # Compare the concatenated forms
            if order1 > order2:
                return -1  # a should come before b
            elif order1 < order2:
                return 1   # b should come before a
            else:
                return 0   # a and b are equivalent
        
        # Sort the array using custom comparison function
        arr.sort(key=functools.cmp_to_key(compare))
        
        # Join the sorted array elements to form the largest number
        return ''.join(arr)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import functools

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(str, input().strip().split()))
        ob = Solution()
        ans = ob.printLargest(n, arr)
        print(ans)
        tc -= 1

# } Driver Code Ends