s = int(input("Enter a Number to find cube root : "))
for i in range(abs(s)+1):
    if i*i*i>=s:
        break
if i*i*i!=abs(s):
    epsilon = 0.01
    low = 0
    high = s
    guess = (low+high)/2.0
    while abs(guess**3 - s) >= epsilon:
        if guess**3 < s:
            low = guess
        else:
            high = guess
        guess = (high+low)/2.0
    print("It is not a perfect cube close to the cube root of",s,"is",guess)
else:
    if s<0:
        i=-i
    print("Cube root of",s,"is",i)
