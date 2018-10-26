list = [int(x) for x in input().split()]
print("The list is",list)
s = set(list)
print(s)
new_list = []
for i in range(len(list)):
    if list[i]%2==0:
        new_list.append(list[i])
print(new_list)
reverse = list[::-1]
print(reverse)
