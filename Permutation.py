
def isPermutation(str1, str2):
# to Get lengths of both strings
    n1 = len(str1)
    print("length of string1",n1)
    n2 = len(str2)
    print("length of string2",n2)


    if (n1 != n2):
        return False

# Sorting both strings
    a = sorted(str1)
    str1 = " ".join(a)
    b = sorted(str2)
    str2 = " ".join(b)

# Comparing
    for i in range(0, n1, 1):
        if (str1[i] != str2[i]):
            return False

    return True

if __name__ == '__main__':
    str1 = input("Enter STRING '1' : \n")
    str2 = input("Enter STRING '2' : \n")
    print(str1)
    print(str2)
    if (isPermutation(str1, str2)):
        print("Yes,IT IS A PERMUTATION")
    else:
        print("No,IT IS NOT A PERMUTATION")

