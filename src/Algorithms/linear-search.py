def linearSearch(searchList, target):
    """
    Returns index position of the target if found else return None.
    """

    for i in range(0, len(searchList)):
        if searchList[i] == target:
            return i

    return None

    # The above is a linear runtime algorithm: O(n) - sequentially goes through the list.


def verifySearch(index):
    if index is not None:
        print("Target found at index: ", str(index))
    else:
        print("Target was not found")


numRange = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = linearSearch(numRange, 8)
verifySearch(result)

result = linearSearch(numRange, 15)
verifySearch(result)
