import sys
import multiply

if __name__ == '__main__':
    a = input("input:")
    
    b1=bin(int(a[0]))[2:]
    b2=bin(int(a[1]))[2:]
    a=""
    if(len(b1)<4):
        c=4-len(b1)
        for x in range(c):
            b1="0"+b1
        #secure 4 bits
    if(len(b2)<4):
        c=4-len(b2)
        for x in range(c):
            b2="0"+b2
    a=b1+b2
    
    print(a)
    for i in range (1,256):
        b=bin(i)[2:]
        r=multiply.mul(a,b)
        if(r!= None):
            break     
    print(r)
    import matrix
    matrix.mat(r)  
           
    