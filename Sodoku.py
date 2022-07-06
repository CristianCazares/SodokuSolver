def showSodoku(matrix):
    block = 3
    print(' ----------------------')

    for _ in range(3):
        for y in range(3):
            block -= 3
            for _ in range(3):
                print(' ', end='')
                for col in range(3):
                    index = matrix[block][col+(3*y)]
                    if(index == 0 or index == '0'):
                        print('_', end=" ")
                    else:
                        print(index, end=" ")

                print('|', end='')
                block += 1
                
            print('')
        block += 3
        print(' ----------------------')
    
def inputFile(fileLocation):
    file = open(fileLocation, 'r').read()
    from re import split
    file = split(' |\n|\||-+', file) #Clean input
    file = ' '.join(file).split()

    block = 0
    count = 0
    sodoku = [ [], [], [], [], [], [], [], [], [] ]
    for i in range(3, len(file)+3, 3):
        sodoku[block].extend(file[i-3:i])
        count += 1
        block += 1
        if (block % 3 == 0):
            block -= 3
        if (count % 9 == 0 and count != 0):
            block += 3

    return sodoku