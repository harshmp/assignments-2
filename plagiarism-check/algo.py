import string

def checker(text1, text2):
    cleanChars = string.letters + string.digits + "- "

    cleanString1 = filter(lambda c : c in cleanChars, text1)
    cleanString2 = filter(lambda c : c in cleanChars, text2)

    bag1 = cleanString1.split()
    bag2 = cleanString2.split()

    if "a" in bag1: bag1.remove("a")
    if "is" in bag1: bag1.remove("is")
    if "in" in bag1: bag1.remove("in")
    if "the" in bag1: bag1.remove("the")

    if "a" in bag2: bag2.remove("a")
    if "is" in bag2: bag2.remove("is")
    if "in" in bag2: bag2.remove("in")
    if "the" in bag2: bag2.remove("the")

    copiedWords = len(set(bag1) & set(bag2))
    similarityFlag = False
    smallerLength = 0

    if len(bag1) <= len(bag2):
        smallerLength = len(bag1)
    else:
        smallerLength = len(bag2)

    if copiedWords >= (0.5 * smallerLength):
        similarityFlag = True

    return similarityFlag

if __name__ == "__main__":
    print("")
