s = input("Enter the password ")
loch = "abcdefghijklmnopqrstuvwxyz"
upch = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = "1234567890"
sy = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
v = True
c=0
if len(s)>=8 and len(s)<=16:
    c+=1
    for i in range(1,len(s)):
        if(s[i]==s[i-1]):
            val=False
            break
    c+=1
    temp = c
    lower = True
    upper = True
    symbols = True
    num = True
    for i in range(len(s)):
        if not val:
            break
        if (s[i] in loch) and (lower):
            c+=1
            lower = False
        elif (s[i] in uoch) and (upper):
            c+=1
            upper = False
        elif (s[i] in n) and (num):
            c+=1
            num = False
        elif (s[i] in sy) and (sy):
            c+=1
            symbols = False
if c==6 and v:
    print("It is a valid password")
else:
    print("It is not a valid password")
