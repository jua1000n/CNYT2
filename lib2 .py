from sys import stdin

def suma(r, i):
    res1 = r[0] + i[0]
    res2 = r[1] + i[1]
    return (round(res1,4), round(res2,4))

def producto(r, i):
    res1 = (r[0] * i[0]) - (r[1] * i[1])
    res2 = (r[0] * i[1]) + (r[1] * i[0])
    return (round(res1,4), round(res2,4))

def multimatin(r,i):
    mat = [[0]*len(i[0]) for h in range(len(r))]
    for y in range(len(r)):
        for j in range(len(i[0])):
            if len(mat)==1:
                long=2
            else:
                long=len(mat)
            for z in range(long):
                mat[y][j]+=r[y][z]*i[z][j]
    return mat

def multimat(r,i):
    mat = [[(0,0)]*len(i[0]) for h in range(len(r))]
    for y in range(len(r)):
        for j in range(len(i[0])):
            if len(mat)==1:
                long=2
            else:
                long=len(mat)
            for z in range(long):
                mat[y][j]=suma(mat[y][j],producto(r[y][z],i[z][j]))
    return mat

def canic(mat,lis,clic):
    res=mat
    if type(mat[0][0])== int:
        for i in range(clic):
            res=multimatin(res,mat)
        return multimatin(res,lis)
    elif type(mat[0][0])== tuple:
        res=multimat(res,i)
        for i in range(clic):
            res=res=multimat(res,mat)
        lista=[(lis[x][0],0) for x in range(len(lis))]
        return multimat(res,lista)
        
        

    
