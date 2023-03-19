#Задание №1
import random
a = int(input('a = '))
b = int(input('b = '))
matrix_1=[[random.randint(1, 11) for j in range(b)] for i in range(a)]
print('Matrix 1:')
for i in range(a):
    print(matrix_1[i])
    matrix_2 = [[random.randint(1, 11) for j in range(b)] for i in range(a)]
    print('Matrix 2: ')
    for i in range(a):
        print(matrix_2[i])
        result = [[matrix_1[i][j] + matrix_2[i][j] for j in range
        (len(matrix_1[0]))] for i in range(len(matrix_1))]
        print("Результат сложения:")
        for r in result:
            print(r)



