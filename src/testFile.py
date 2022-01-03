print("Python is EZ" + " " + str(2 + 2))

newVar = "new variable"
numVar = 5

print("variables:" + newVar, " " + str(numVar))

varRange = newVar[4:7]
newList = [1, 2, 3, "one", "two", "three"]

print(varRange)

# You can grab a range or exact index from a list w/ [ index : index ]

print(newList[0])
print(newList[3])
print(newList[1])
print(newList[4:6])
print(newList[3:5])

newList.append(newVar)

dictionary = {"Name": "Darrell", "Height": 5.7}
bigTuple = ("tup1", "tup2")

print(dictionary, bigTuple)


# loops & conditionals

while numVar > 0:
    print("runs left:" + str(numVar - 1))
    numVar -= 1

for i in range(0, 5):
    print("run count:" + str(i))

for item in newList:
    print(item)

if numVar > 5:
    print("should be 5")

elif numVar > 5:
    print("should be 5")

else:
    print("its 5")


# Functions
def printGreatness(whoIsGreat):
    print(whoIsGreat, "You are Great!")


printGreatness("K7NG")
