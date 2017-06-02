"""
Q: Given two strings, check whether they are anagrams of each other.
Example: "public relations" is an anagram of "crap built on lies."
You are also given a testing client to check the correctness of your function."""

#Testing client for anagram

class AnagramTesting(object):

    def Client(self,sol):
        assert(sol('go go go','gggooo')==True)
        assert(sol('abc','cba')==True)
        assert(sol('hi man','hi     man')==True)
        assert(sol('aabbcc','aabbc')==False)
        assert(sol('123','1 2')==False)
        print("ALL TEST CASES PASSED")

#Solution:

def anagram(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()
    if len(s1) != len(s2):
        return False

    count = {}

    for letter in s1:
        if letter in count:
            count[letter] +=1
        else:
            count[letter] = 1

    for letter in s1:
        if letter in count:
            count[letter] -=1
        else:
            count[letter] = 1

    for keys in count:
        if count[keys] !=0:
            return False

    return True

#Test the function
t = AnagramTesting()
t.Client(anagram)
