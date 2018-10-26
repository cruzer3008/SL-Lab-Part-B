def maximum(list):
    length = len(list)
    if length==1:
        return list
    elif list[length-1]>=list[length-2]:
        del list[length-2]
    elif list[length-1]<=list[length-2]:
        del list[length-1]
    return maximum(list)

print("Enter the numbers to be considered below")
list = [int(x) for x in input().split()]
print("The entered elements are",list)
print(maximum(list))

