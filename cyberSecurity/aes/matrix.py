def mat(b):
    import numpy as np
    z=np.array([    [1,0,0,0,1,1,1,1],[1,1,0,0,0,1,1,1],[1,1,1,0,0,0,1,1],[1,1,1,1,0,0,0,1],[1,1,1,1,1,0,0,0],[0,1,1,1,1,1,0,0],[0,0,1,1,1,1,1,0],[0,0,0,1,1,1,1,1] ])
    b1=list(b)[::-1]#reverse list
    for i in range (len(b1)):
        b1[i]=int(b1[i])
        #str 2 int
    if(len(b1)!=8):#if it's not 8 bits
        for i in range (len(b1),8):
            b1.append(0)
    b1= np.matmul(z,b1)#matrix multiply
    
    for i in range (len(b1)):#turn * 2 xor
        if(b1[i]%2==0):
            b1[i]=0
        elif(b1[i]%2==1):
            b1[i]=1
        else:
            pass

    y=[1,1,0,0,0,1,1,0]#63

    f=list(  (b1^y) [::-1])
    str_f1=""
    str_f2=""
    for i in range(4):
        str_f1+=str(f[i])
        #2 hex
    for i in range(4,len(f)):
        str_f2+=str(f[i])

    print(hex(  int (str_f1,2))[2:] ,   hex(  int (str_f2,2))[2:])
   