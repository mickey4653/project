p=59
q=83
e=17
fi=(p-1)*(q-1)
print("fi(n)=",fi)
def inverse(e,fi):
    i=1
    while(i!=0):
        if((i*e)%fi==1):
            return i
            break
        else:
            i+=1   
i=inverse(e,fi)
    
print("private key=",i)

