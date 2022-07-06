def showSodoku(matrix):
    cell = 3
    print(' ----------------------')

    for _ in range(3):
        for y in range(3):
            cell -= 3
            for _ in range(3):
                print(' ', end='')
                for col in range(3):
                    index = matrix[cell][col+(3*y)]
                    if(index == 0):
                        print('_', end=" ")
                    else:
                        print(index, end=" ")

                print('|', end='')
                cell += 1
                
            print('')
        cell += 3
        print(' ----------------------')

    

sodoku = [
    list(range(1, 10)),
    list(range(1, 10)),
    list(range(1, 10)),
    list(range(1, 10)),
    list(range(1, 10)),
    list(range(1, 10)),
    list(range(1, 10)),
    list(range(1, 10)),
    list(range(1, 10)),
]

showSodoku(sodoku)

print("\n\n")
sodoku = [
    [0,6,0,
    0,4,0,
    0,0,0],
    [0,0,0,
    8,0,5,
    0,0,0],
    [0,1,7,
    3,0,2,
    8,6,0],
    
    [2,0,0,
    0,5,0,
    6,7,0],
    [0,0,4,
    0,2,7,
    0,5,3],
    [0,0,0,
    6,0,0,
    4,0,0],

    [0,3,0,
    0,0,0,
    0,0,9],
    [0,0,0,
    5,0,0,
    0,0,0],
    [0,0,0,
    0,0,1,
    0,0,0],
]

showSodoku(sodoku)