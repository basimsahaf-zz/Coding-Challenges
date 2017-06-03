# -*- coding: utf-8 -*-
# Q: Given a string of opening and closing parentheses, check whether it’s balanced.
# We have 3 types of parentheses: round brackets: (), square brackets: [], and curly
# brackets:. Assume that the string doesn’t contain any other character than these,
# no spaces words or numbers. As a reminder, balanced parentheses require every opening
# parenthesis to be closed in the reverse order opened. For example ‘([])’ is balanced
# but ‘([)]’ is not.
#
# You can assume the input string has no spaces.

#Testing Client:

from stack import stack

class TestBalanceCheck(object):

    def Client(self, sol):
        assert(sol('[()]')==True)
        assert(sol('[(])')==False)
        #assert(sol(')][(')==False)
        assert(sol('[({{(){}}})]')==True)
        assert(sol(')')==False)
        assert(sol('')==True)
        print("ALL TEST CASES PASSED")


#Solution:
def balance_check(str1):

    if len(str1)%2 != 0 or len(str1)==1:
        return False

    seq1 = ['(', '[', '{']
    seq2 = [')', ']', '}']

    s = stack()

    for i in str1:
        if i in seq1:
            s.push(seq2[seq1.index(i)])
        elif s.size()==0 or i != s.peek():
            return False
        else:
            s.pop()
    return True

testObject = TestBalanceCheck()
testObject.Client(balance_check)
