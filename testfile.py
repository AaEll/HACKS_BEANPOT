import musicalpdb
from functools import reduce
musicalpdb.my_set_trace

x = 0
def my_func():
    global x
    x+=1
    print(x)

for i in range(1,4):
    my_func()

y = 0
while (x<y):
    y = x+2
    my_func()
    y = y%11

z = [1,'2',3,4,5]
w = reduce(lambda x,y : x+y, z)
for i in w :
    print(i)

def assertIsValidObjectParameterStatementForCurrentString(myStr):
    for i in range(len(myStr)):
        if(myStr[i] in "aeiouy"):
            print("probably a vowel, but checking real quick")
            if(isItReallyAVowel(myStr[i])):
                return True
    
    print("no vowels found! this is a FAKE WORD.")
    return False

def isItReallyAVowel(myChar):
    if(myChar in "aeiou"):
        return True
    
    return False

assertIsValidObjectParameterStatementForCurrentString('1241231231231asdfasdfasdf')
