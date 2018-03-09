#!usr/bin/python3


def isListOfInts(x):
    if(type(x) is not list):
        raise ValueError(str(x) + " - arg not of <list> type")
    else:
        if len(x) is 0:
            return True
        else:
            f = 1
            for i in x:
                if(type(i) is not int):
                    f = 0
            if (f == 1):
                return True
            else:
                return False


def testList(a):
    print(isListOfInts(a))


testList([])
testList([1])
testList([1, 2])
testList([0])
testList(['1'])
testList([1, 'a'])
testList(['a', 1])
testList([1, 1.])
testList([1., 1.])
testList((1, 2))
