# =============================================================================
# Suppose insertion sort is expressed as a recursive procedure as follows: In order to sort A[1..n],
# we recursively sort A[1..n-1] and then insert A[n] into the sorted array A[1..n-1].
# Write a recurrence for the running time of this recursive version of insertion sort.
# =============================================================================
def sort(A,sortA,key):#A,key
        while(key<=len(A)-1):# go through all elements in A
            sortA.append(A[key])
            for r in range(key,0 and r-1>=0,-1):
                    l=r-1
                    if(sortA[r]>= sortA[l]):
                            temp=sortA[l]
                            sortA[l]=sortA[r]
                            sortA[r]=temp
                            if(r==1):
                                 key+=1
                                 sort(A,sortA,key)
                                
                            
                    else:
                        key+=1
                        sort(A,sortA,key)
                        break
            break
def sortedArray(sortA):
    print("\nsorted array")
    for x in range(len(sortA)):
        print(sortA[x], end=",")
    
def originalArray(A):
    print("original array")
    for x in range(len(A)):
        print(A[x], end=",")
    
if __name__ =="__main__":
    A=[3,10,-2,0,7,2,5,9,1,7]
    sortA=[A[0]]
    key=1
    originalArray(A)
    sort(A,sortA,key)
    sortedArray(sortA)
