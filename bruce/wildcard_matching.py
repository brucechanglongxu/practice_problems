class Solution:
"""
Dynamic Programming Solution for Wildcard Matching 
"""
        def strrmatch(self, strr : str, pattern : str, n, m) -> bool:
        """
        Inputs : String strr that we search for some pattern pattern, with lengths n and m respectively
        Parameters : strr (string), pattern (string)
        Output: Boolean value which indicates whether pattern matches our string with the wildcard matching rules
        Space Complexity: Minimum between len(pattern) and len(strr) 
        Time Complexity: Dependent on number of stars and question marks 
        """
        # empty pattern can only match with
        # empty string
         if (m == 0):
             return (n == 0)

         # lookup table for storing results of
         # subproblems
         lookup = [[False for i in range(m + 1)] for j in range(n + 1)]

         # empty pattern can match with empty string
         lookup[0][0] = True

         # Only '*' can match with empty string
         for j in range(1, m + 1):
             if (pattern[j - 1] == '*'):
                 lookup[0][j] = lookup[0][j - 1]

         # fill the table in bottom-up fashion
         for i in range(1, n + 1):
             for j in range(1, m + 1):

                 # Two cases if we see a '*'
                 # a) We ignore ‘*’ character and move
                 # to next character in the pattern,
                 # i.e., ‘*’ indicates an empty sequence.
                 # b) '*' character matches with ith
                 # character in input
                 if (pattern[j - 1] == '*'):
                     lookup[i][j] = lookup[i][j - 1] or lookup[i - 1][j]

                 # Current characters are considered as
                 # matching in two cases
                 # (a) current character of pattern is '?'
                 # (b) characters actually match
                 else if (pattern[j - 1] == '?' or strr[i - 1] == pattern[j - 1]):
                     lookup[i][j] = lookup[i - 1][j - 1]

                 # If characters don't match
                 else:
                     lookup[i][j] = False

         return lookup[n][m]
