Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#User function Template for python3


class Solution:
    def computeLPSArray(self, pattern):
        """
        Computes the Longest Prefix Suffix (LPS) array for the given pattern.
        """
        m = len(pattern)
        lps = [0] * m
        length = 0  # Length of the previous longest prefix suffix
        i = 1

        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def search(self, pattern, text):
        """
        Finds all occurrences of pattern in the text using the KMP algorithm.
        """
        m = len(pattern)
        n = len(text)
        lps = self.computeLPSArray(pattern)
        indexes = []

        i = 0  # Index for text[]
        j = 0  # Index for pattern[]

        while i < n:
            if pattern[j] == text[i]:
                i += 1
                j += 1

            if j == m:
                indexes.append(i - j + 1)
                j = lps[j - 1]

            # Mismatch after j matches
            elif i < n and pattern[j] != text[i]:
                # Do not match lps[0..lps[j-1]] characters, they will match anyway
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return indexes


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        for value in ans:
            print(value,end = ' ')
        print()
# } Driver Code Ends