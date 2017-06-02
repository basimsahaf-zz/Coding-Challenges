"""
Q: Given a string in the form 'AAAABBBBCCCCCDDEEEE' compress it to become 'A4B4C5D2E4'.
For this problem, you can falsely "compress" strings of single or double letters. For instance,
it is okay for 'AAB' to return 'A2B1' even though this technically takes more space.

The function should also be case sensitive, so that a string 'AAAaaa' returns 'A3a3'.
"""

class CompressTest(object):

    def compressClient(self,sol):
        assert(sol('') == '')
        #assert(sol('AABBCC') =='A2B2C2')
        assert(sol('AAABCCDDDDD') == 'A3B1C2D5')
        print('ALL TEST CASES PASSED')
# Solution: First attempt

def compress2(str1):
    count = {}
    unique =[]
    for i in str1:
        if i not in unique:
            unique.append(i)
        if i in count:
            count[i] +=1
        else:
            count[i] = 1

    word = ''
    for key in unique:
        word +=key
        word += str(count[key])
    return word

#Tests
t = CompressTest()
t.compressClient(compress2)



# Most Efficient one
def compress(str1):

    if len(str1)==0:
        return ""
    if len(str1)==1:
        return s + "1"

    count = 1
    index = 1
    leng = len(str1)
    word =""

    while(index < leng):

        if str1[index]==str1[index-1]:
            count +=1
        else:
            word = word + str1[index-1] +str(count)
            count = 1

        index += 1
    word = word + str1[index-1] +str(count)
    return word

#Tests
t = CompressTest()
t.compressClient(compress)
