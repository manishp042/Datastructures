sequence = [34,45,21,32,65,23,76,12,10,15]
def quickSort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()
    items_lower = []
    items_greater = []
    for item in sequence:
        if item < pivot:
            items_lower.append(item)
        else:
            items_greater.append(item)
    return quickSort(items_lower)+ [pivot]+ quickSort(items_greater)
    
print(quickSort(sequence))
