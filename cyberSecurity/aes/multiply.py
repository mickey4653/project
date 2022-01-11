
def mul(a1,b1):
    from numpy.polynomial.polynomial import Polynomial
    import numpy as np
    str1 =[]
    str2=[]
    for i in range (0,len(a1)):
        str1.append(int (a1[ (len(a1))   -1-i]) )
        #NUM 2 array
    str1=np.array(str1)
    p1 = Polynomial(str1)

    for i in range (0,len(b1)):
        str2.append(int (   b1[ (   len(b1) )   -1-i]   )    )
    
    str2=np.array(str2)
    p2 = Polynomial(str2)

    p3= Polynomial( [1,1,0,1,1,0,0,0,1]  )
    str_final=str((p1*p2) %p3 )

    str_final=str_final.replace("poly([","")    
    str_final=str_final.replace("])","")
    str_final=str_final.replace(".","")
    str_final=str_final.replace("-","")
    str_final=str_final.replace(" ","")
    str_final=list(str_final)
    for i in range (len(str_final)):
        if( int(str_final[i])%2==0):
            str_final[i]="0"
        elif(int(str_final[i])%2==1):#odd
            str_final[i]="1"
            #substite other num to 0
    str_final="".join(str_final)
    #2 string
    if(str_final.rfind("1")==0):
        return b1
        #check if is 1
    
