import operator

class py_solution():
    def reverse_words(self,s):
        return " ".join(reversed(s.split()))
    def vowel_count(self,s):
        vowel = 0
        for i in range(len(s)):
            if s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u"or s[i]=="A"or s[i]=="E"or s[i]=="I" or s[i]=="O" or s[i]=="O":
                vowel+=1
        return vowel

myDict = {}

firstString = input("Enter the first string\n")
firstStringReverse = py_solution().reverse_words(firstString)
firstStringVowels = py_solution().vowel_count(firstString)

secondString = input("Enter the second string\n")
secondStringReverse = py_solution().reverse_words(secondString)
secondStringVowels = py_solution().vowel_count(secondString)

thirdString = input("Enter the third string\n")
thirdStringReverse = py_solution().reverse_words(thirdString)
thirdStringVowels = py_solution().vowel_count(thirdString)

myDict[firstStringReverse] = firstStringVowels
myDict[secondStringReverse] = secondStringVowels
myDict[thirdStringReverse] = thirdStringVowels

sorted_dict = dict(sorted(myDict.items()))

print(sorted_dict)
