Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#User function Template for python3


class Solution:
    def firstElementKTime(self, n, k, a):
        # Create a dictionary to store element counts.
        count_dict = {}
        for element in a:
            # Increment the count of the current element.
            count_dict[element] = count_dict.get(element, 0) + 1

            # Check if the current element count is equal to k and return it.
            if count_dict[element] == k:
                return element

        # If no element occurs k times, return -1.
        return -1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, k = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstElementKTime(n, k, a))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends