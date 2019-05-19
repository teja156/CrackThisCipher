st = raw_input("Enter the string : ")


res = ""
p = 10799
q = 863
n = p*q
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
        
print("Cipher string : %s"%res)
