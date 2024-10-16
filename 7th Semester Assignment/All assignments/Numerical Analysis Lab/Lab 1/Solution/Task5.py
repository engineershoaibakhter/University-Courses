def getMatrix(row,col):
    mat=[]
    for i in range(row):
        r=[]
        for j in range(col):
            n=int(input(f'Input element at position ({i+1},{j+1}): '))
            r.append(n)
        mat.append(r)
    return mat

def printMatrix(mat):
    for row in mat:
        print(' '.join(map(str,row)))


def Addition(matA,matB,r1,c1):
    res=[]
    for i in range(r1):
        row=[]
        for j in range(c1):
            row.append(matA[i][j]+matB[i][j])

        res.append(row)

    return res

def Subtraction(matA,matB,r1,c1):
    res=[]
    for i in range(r1):
        row=[]
        for j in range(c1):
            row.append(matA[i][j]-matB[i][j])

        res.append(row)

    return res

def Multiplication(matA,matB,r1,r2,c1,c2):
    # if(c1==r2):
    #     # res=[r1][c2]
        res=[]
        for i in range(r1):
            t_res=[]
            for j in range(c2):
                temp=0
                for k in range(c1):
                    temp+=matA[i][k]*matB[k][j]
                t_res.append(temp)
            res.append(t_res)

        return res
    # else:
    #     return None

r1=2
c1=2

r2=2
c2=2

matA=getMatrix(r1,c1)

print('Matrix A: ')
printMatrix(matA)

matB=getMatrix(r2,c2)
print('Matrix B: ')
printMatrix(matB)

print('Addition: ')
printMatrix(Addition(matA,matB,r1,c1))

print('Subtraction: ')
printMatrix(Subtraction(matA,matB,r1,c1))


print('Multiplication: ')
printMatrix(Multiplication(matA,matB,r1,r2,c1,c2))