def binarySearch(searchList: list, target):
    """
    Returns index position of the target if found else return None.
    """
    first = 0
    last = len(searchList) - 1
    # 1. Start at the middle of the searchList'
    while first <= last:
        midPoint = (first + last)//2
    # 2. Check if target is above or below middle value
        if searchList[midPoint] == target:
            return midPoint
        elif searchList[midPoint] < target:
            first = midPoint + 1
        else:
            first = midPoint - 1
    return None

    # The above is a Logarithmic runtime algorithm: O(log n) - The while runs until target is found & each run shrinks the sample size.


def verifySearch(index):
    if index is not None:
        print("Target found at index:", str(index))
    else:
        print("Target was not found")


numRange = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = binarySearch(numRange, 8)
verifySearch(result)

result = binarySearch(numRange, 15)
verifySearch(result)


# Recursive version
def recursiveVersion(searchList, target):
    if (len(searchList) == 0):
        return False
    else:
        midPoint = len(searchList)//2

        if searchList[midPoint] == target:
            return True
        else:
            if searchList[midPoint] < target:
                return recursiveVersion(searchList[midPoint + 1:], target)
            else:
                return recursiveVersion(searchList[:midPoint], target)


def verifyRecursiveVersion(found: bool):
    if found:
        print("Target found:", str(found))
    else:
        print("Target was not found", str(found))


result = recursiveVersion(numRange, 8)
verifyRecursiveVersion(result)

result = recursiveVersion(numRange, 15)
verifyRecursiveVersion(result)
