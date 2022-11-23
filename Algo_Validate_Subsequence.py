arr = [2, 1, 32, 7, 6, -1, 3, 10]
sub = [1, 6, -1, 10]

def firstValidate(array, sequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)


def secondValidate(array, sequence):
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence)

# print(firstValidate(array = arr, sequence = sub))
# print(secondValidate(array = arr, sequence = sub))