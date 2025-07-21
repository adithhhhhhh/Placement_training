#spiral matrix
matrix=[
    [1,2,3,4],
    [4,5,6,7],
    [7,8,9,10],
    ]
rows=len(matrix)
cols=len(matrix[0])
left=0
right=cols-1
top=0
bottom=rows-1
while(top<=bottom and left<=right):
    for i in range(left,right+1):
        print(matrix[top][i],end=" ")
    top=top+1
    for i in range(top,bottom+1):
        print(matrix[i][right],end=" ")
    right=right-1
    if(top<=bottom):
        for i in range(right,left-1,-1):
            print(matrix[bottom][i],end=" ")
        bottom=bottom-1
    if(left<=right):
        for i in range(bottom,top-1,-1):
            print(matrix[i][left],end=" ")
        left=left+1