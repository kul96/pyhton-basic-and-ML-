s1 = input()
word = s1.split(' ')
print(word)
#if(s1[1]=="morning")
#print(s1[-1])
emogi = {
    ":)":"a",
    ":(":"b",

}
re = ""
for i in range(len(word)-1):
    re = re + word[i] + " "
re = re + emogi[word[-1]]
print(re)
