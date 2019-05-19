import sys
cipher = "II!26!32%!1I%!32%A!32"
st = raw_input("Enter string : ")
if(st[1]!='R' or len(st)!=12):
    print("Wrong!")
    sys.exit(0)
    
def enc(n):
    res = ""
    for i in st:
        #print("char %c"%i)
        asc = ord(i)
        temp = n%asc
        #print("temp %d"%temp)
        if(temp<33):
            diff = 33-temp
            res = res + chr(33) + str(diff)
            #print("adding %c and %s"%(chr(33),str(diff)))
        elif(temp>126):
            diff = temp - 126
            res = res + chr(126) + str(diff)
            #print("adding %c and %s"%(chr(126),str(diff)))
        elif(temp>=33 and temp<=126):
            res = res + chr(temp)
            #print("adding %c"%(chr(temp)))
    
    if(res==cipher):
        return True
    else:
        return False


    
#First get all the prime numbers within the given range
primes = list()
prime = True
for i in range(3,11084):
    prime = True
    for j in range(2,i):
        if(i%j==0):
            prime = False
            break
    if(prime):
        primes.append(i)

        
#print(str(primes))

possible_primes = list()



#Now extract the possible values of 'n' based on the condition n%82==73
for i in range (0,len(primes)):
    p = primes[i]
    for j in range(0,len(primes)):
        q = primes[j]
        n = p*q
        if(n%82==73):
            
            possible_primes.append(n)
            
            #print("n = %d, p = %d, q = %d"%(n,p,q))
            

print("Total possible prime pairs : %d"%len(possible_primes))
            

#For each possible value of n, check if the string forms the encrypted form same as cipher
for i in possible_primes:
    isPossible = enc(i)
    if(isPossible):
        print("Possible string!")
        sys.exit()
        

        
print("Not possible!")
    
