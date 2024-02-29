Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#User function Template for python3
class Solution:
    def sumBitDifferences(self, arr, n):
        # Initialize the result
        result = 0

        # Traverse over all bits
        for i in range(32):
            # Count the number of elements with i'th bit set
            count_set_bit = 0
            for j in range(n):
                if (arr[j] & (1 << i)):
                    count_set_bit += 1

            # Count the number of elements with i'th bit unset
            count_unset_bit = n - count_set_bit

            # Add the bit differences for this position to the result
            result += count_set_bit * count_unset_bit * 2

        return result


#{ 
 # Driver Code Starts

#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.sumBitDifferences(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends