Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#User function Template for python3

class Solution:
    def generate_subsequences(self, s, idx, curr, result):
        if idx == len(s):
            if curr:
                result.append("".join(curr))
            return
        # Include the current character
        self.generate_subsequences(s, idx + 1, curr + [s[idx]], result)
        # Exclude the current character
        self.generate_subsequences(s, idx + 1, curr, result)

    def AllPossibleStrings(self, s):
        result = []
        self.generate_subsequences(s, 0, [], result)
        return sorted(result)
#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends