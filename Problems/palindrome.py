"""Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
"""
#  Palindrome: a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam or nurses run.

s = 'radkar'
"""
def solution(s):
    for i in range(len(s)):
        t = s[:i] + s[i+1:]
        if t == t[::-1]:  #check t and t in reverse
            return True
    return False
"""
def solution(s):
    if s==s[::-1]:
        return True
    return False

print(solution(s))
