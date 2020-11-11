# Gous eleme methodu ile matris çözümü bulmak

def printMatrix(matrix):
    print("-----------------")
    for row in matrix:
        print(row)
    print("-----------------")


def createMatrix(c,r, init):
    return [[init for i in range(c)] for j in range(r)]    


# Bu fonksiyon sayesinde matrix satırları sıralanır
def sortMatrix(matrix, index):
    m = []
    lenght = len(matrix)

    for i in range(index, lenght):
        row = matrix[i]
        if row[index] == 0:
            m.insert(lenght, row) 
        else:
            m.insert(0, row)

    
    matrix[index : lenght] = m
    return matrix 

def gaussEleminate():
    isResult = True
    #hesaplanacak matris burada  girileektir
    
    #hesaplanacak matris bu kısma yazılmalı 
    #fazladan olan son sütün cevaplar. 
    #x + 2y + 3z = 1 gibi
    
    matrix = [
        [1,	 2,	 3,	    1],
        [10, 20, 11,    5],
        [2, 8, 42,      6],
    ]
    
    """
    3x3 lük matrisleri çözdü
    4x4 lük matrsileri çözdü

    matrix = [
        [1,	 2,	 3,	 1],
        [10, 20, 11, 5],
        [2, 8, 42, 6],
    ]
    matrix = [
        [8,0,3,4,14],
        [0,7,8,3,20],
        [4,5,1,2,42],
        [9,0,7,0,86]
    ]

    matrix = [
        [1,2,3,4,5,6],
        [6,7,45,0,25,6],
        [7,10,0,8,2,14],
        [1,2,3,4,5,51],
        [3,0,4,2,14,20]
    ]

    """
    n = len(matrix)

    result = createMatrix(1,n, 0)



    # bu işlem ardından matrisimiz son halini alacaktır
    for i in range(n):
        matrix = sortMatrix(matrix, i)

        if matrix[i][i] != 1 :
            val = matrix[i][i]
            if val == 0 :
                print("bu matrisin sonsuz çözümü var")
                isResult = False
                break
            if val != 1:
                for k in range((n+1)):
                    matrix[i][k] = matrix[i][k]/val 

        for j in range((i + 1), n):
            val = -(matrix[j][i])
            
            for k in range(i,(n+1)):
                a = matrix[j][k] + (matrix[i][k] * val)
                if a == 0 :
                    matrix[j][k] = 0
                else:
                    matrix[j][k] = a 

    if isResult == False:
        return 1
    last = matrix[(n-1)][(n-1)]

    if last == 0:
        print("sonsuz çözüm vardır!")

    else:
        result.insert((n-1), matrix[(n-1)][n])
    i = (n-1)
    while (i != 0):
        j = i - 1
        val = 0
        
        for k in range(i, n):
            val +=(matrix[j][k] * result[k])

        result[j] = matrix[j][n] - val
        i-=1



    printMatrix(matrix)
    printMatrix(result)
        

def main():

    gaussEleminate()
    

main()
