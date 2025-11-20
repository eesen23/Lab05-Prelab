def longest_palindromic_substring(s):
    """
    Given a string find the longest palindromic substring
    """
    if len(s) < 2 :
        return ""
    
    longest = ""
    
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub = s[i:j]
            
            if len(sub) >= 2 and sub == sub[::-1]:
                if len(sub) > len(longest):
                    longest = sub
                    
    return longest