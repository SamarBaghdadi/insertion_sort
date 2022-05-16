
def insertion_sort(A):
    if A[0]>A[1]:
        A[0],A[1]=A[1],A[0]
    for index in range(1,len(A)):
        if A[index]<A[index-1]:
            my_bool=True
            j=index-1
            inter_bool= False
            while my_bool==True:
                if A[index]>A[j]:
                    my_bool=False
                    inter_bool=True
                elif j==0:
                        my_bool=False
                else:
                    j=j-1
            temp=A[index]
            if inter_bool==True:
                for sw in range(index,j+1,-1):
                    A[sw]=A[sw-1]
                A[j+1]=temp
            else:
                for sw in range(index,j,-1):
                    A[sw]=A[sw-1]
                A[j]=temp
    return A

