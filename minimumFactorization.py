def smallestFactorization(a):
        seen =[]
        req = []
        arr = []

        for i in range(1,10):

            if(a%i==0):
                reqNum = int(a/i)
                if reqNum in req:
                    outPut = int(str(min(reqNum,i))+str(max(reqNum,i)))
                    arr.append(outPut)

                else:
                    req.append(i)

        arr.sort()
        print(arr)
        if(len(arr)):
            return arr[0]
        else:
            return 0

print(smallestFactorization(48))
