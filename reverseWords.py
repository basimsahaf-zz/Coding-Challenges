"""
Q: Given a string of words, reverse all the words.
Example: 'Hello my name is John' becomes 'John is name my Hello'
Special consideration: Remove all leading and trailing whitespaces.
Example:
'   Hello John    how are you   '  becomes  'you are how John Hello'

You are also given a testing client for this function.
"""
#Testing Client

class TestingReverse(object):

    def Client(self,sol):
        assert(rev_words('    space before')=='before space')
        assert(rev_words('space after     ')=='after space')
        assert(rev_words('   Hello John    how are you   ')=='you are how John Hello')
        assert(rev_words('1')=='1')
        print("ALL TESTS PASSED")

#Solution:

def rev_words(sentence):
    sentence = sentence.strip()
    #print(sentence)
    arr =[]
    word = ''
    for i in sentence:
        if i == ' ':
            if(word !=''):
                arr.append(word)
            word = ''
        else:
            word +=i
    arr.append(word)
    word = ''
    length = len(arr)-1

    while(length >= 0):
        word +=arr[length]
        if(length!=0):
            word += " "
        length -= 1

    return word

#Testing Client
t = TestingReverse()
t.Client(rev_words)
