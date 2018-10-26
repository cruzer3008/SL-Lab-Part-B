from collections import Counter
from functools import reduce

def word_count(fname):
    with open(fname) as f:
        return Counter(f.read().split())
myDict = word_count("myFile.txt")
print(myDict)

sorted_dict = {}
for w in sorted(myDict, key=myDict.get, reverse=True):
    sorted_dict[w] = myDict[w]
print(sorted_dict)

print(list(sorted_dict.keys())[0:10])
list_number = list(sorted_dict.values())
print(list_number)

print('Average Length',reduce(lambda x,y:x+y,list_number)/(len(list_number)))

print('Squares of ODD numbers',[x*x for x in list_number if x%2!=0])
