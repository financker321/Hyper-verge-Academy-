t= int(input("Enter the dividend : "))
k = 1
print("The divisors of",t)
while k<=t//2 :
    if(t%k==0):
        print(k)
    k+=1
print(t)
