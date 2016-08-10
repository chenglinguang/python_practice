#!/usr/bin/env python3

#-*-encoding:utf-8-*-

'''
Given a string, find the length of the longest substring without repeating characters.
Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
    def lengthOfLongestSubstring(self,s):
        """
        :type s: str
        :rtype: int
        """
        left,right=0,0
        maxCount=0
        d={}
        while right<len(s):
            if s[right] in d and d[s[right]]>=left:
                maxCount=maxCount if maxCount>=(right-left) else (right-left)
                left=d[s[right]]+1
            d[s[right]]=right 
            right+=1
        maxCount=maxCount if maxCount>=(right-left) else (right-left)
        return maxCount


#s='abcdecbf'
#print(lengthOfLongestSubstring(s))
 
                
