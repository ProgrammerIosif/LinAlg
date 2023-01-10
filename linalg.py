from fractions import Fraction
import os

#elementary reduction matrices
erm = []

def display(matrix):
    for row in matrix:
        for column,entry in enumerate(row):

            #add bar for augmented matrix
            # if column == len(row)-1:
            #     print(' |',end='')
            
            #add space to positive numbers to balance '-'
            if entry >= 0:
                print(' ',end='')

            #display entry according to its format
            if isinstance(entry,int):
                print('  ' + str(entry),end=' ')
            elif entry.denominator == 1:
                print('  ' + str(entry.numerator),end=' ')
            else:
                print(str(entry.numerator) + '/' + str(entry.denominator),end=' ')

        print()
        

def swap(matrix):

    display(matrix)

    #read input
    print('first row:',end='')
    x = int(input()) - 1
    print('second row:',end='')
    y = int(input()) - 1

    #swap rows
    aux = matrix[x]
    matrix[x] = matrix[y]
    matrix[y] = aux

    #create permutaion matrix
    i = idMatrix(len(matrix))
    aux = i[x]
    i[x] = i[y]
    i[y] = aux
    erm.append(i)

def scale(matrix):

    display(matrix)

    #read input
    print('scalar:',end='')
    m = input()
    print('row to scale:',end='')
    rowX = int(input()) - 1

    #scale rowX
    for i in range(0,len(matrix[rowX])):
        matrix[rowX][i] *= Fraction(m)

    #create permutaion matrix
    id = idMatrix(len(matrix))
    for i in (range(0,len(id[rowX]))):
        id[rowX][i] *= Fraction(m)
    erm.append(id)

def combination(matrix):

    display(matrix)

    #read input
    print('scalar:',end='')
    m = input()
    print('row to add:',end='')
    rowX = int(input()) - 1
    print('row to be modified:',end='')
    rowY = int(input()) - 1

    #add scaled rowX to rowY 
    for i in range(0,len(matrix[rowX])):
        matrix[rowY][i] += matrix[rowX][i] * Fraction(m)

    #create permutation matrix
    id = idMatrix(len(matrix))
    for i in range(0,len(id[rowX])):
        id[rowY][i] += id[rowX][i] * Fraction(m)
    erm.append(id)
    
def write(matrix):
    #read dimensions
    rows = int(input('number of rows: '))
    cols = int(input('number of columns: '))

    #read the entries
    for row in range(0,rows):
        matrix.append([])
        for col in range(0,cols):
            x = input('matrix['+str(row+1)+']['+str(col+1)+']')
            matrix[row].append(Fraction(x))

def idMatrix(rows):
    i = [[]]
    rows -= 1
    for row in range(0,rows):
        i.append([])
        for col in range(0,rows):
            x = 0
            if row == col:
                x = 1
            i[row].append(Fraction(x))
    return i

def displayERM():
    for i in range(len(erm)-1,-1,-1):
        display(erm[i])

def matrixProduct(m1,m2):
    result = [[]]
    for i in range(0,len(m1)-1):
        result.append([])
        for j in range(0,len(m1)-1):
            s = 0
            for k in range (0,len(m1)-1):
                s += m1[i][k] * m2[k][j]
            result[i].append(s)
    return result
            
                

def inverse():
    m = [[1,0,0],[0,1,0],[0,0,1]]
    for i in erm:
        m = matrixProduct(i,m)
    print("Inverse")
    display(m)

def main():
    os.system('clear')
    #matrix to be used
    a = [[]]
    write(a)
    os.system('clear')

    while True:
        display(a)
        #read input 
        print('1.swap')
        print('2.scale')
        print('3.combination')
        print('0.exit')
        operation = input()

        #choose operation
        if operation == '1':
            swap(a)
        if operation == '2':
            scale(a)
        if operation == '3':
            combination(a)
        if operation == '0':
            displayERM()
            display(a)
            inverse()
            break

if __name__ == '__main__':
    main()
