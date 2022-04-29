from fractions import Fraction
import os

def display(matrix):
    os.system('clear')
    for row in matrix:
        for column,entry in enumerate(row):

            #add delimitor between variables and constants
            if column == len(row)-1:
                print(' |',end='')
            
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


def main():

    #matrix to be used
    a = [[2,1,-1,2],[2,0,1,3],[1,-1,0,0]] 

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
            display(a)
            break

if __name__ == '__main__':
    main()