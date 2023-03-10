# Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту,
# орбита которой имеет самую большую площадь. Напишите функцию f ind_farthest_orbit(list_of_orbits),
# которая среди списка орбит планет найдет ту, по которой вращается самая далекая планета.
# Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, зато искусственные
# спутники были были запущены на круговые орбиты. Результатом функции должен быть кортеж, содержащий
# длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя кортеж
# из пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи используйте списочные выражения.
# Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса,
# а затем найти и сам эллипс, имеющий такую  площадь. Гарантируется, что самая далекая планета ровно одна

import math
import random

list_of_orbits = [(random.randint(4, 10), random.randint(5, 10)) for _ in range(10)]
print(f'Орбиты планет и спутников: {list_of_orbits}')

def find_farthest_orbit (list_of_orbits):
    list_of_planets = list(filter(lambda x: x[0] != x[1], list_of_orbits))
    print(f'Орбиты планет: {list_of_planets}')
    list_of_square = list(enumerate(map(lambda x: round(math.pi * x[0] * x[1], 2), list_of_planets), 1))
    print((f'Площади орбит планет: {list_of_square}'))
    result = list(zip(list_of_planets, list_of_square))
    #print(result)
    return result

list_of_square = find_farthest_orbit(list_of_orbits)

max_square = list_of_square[0]
for max in list_of_square:
    if max_square[1][1] < max[1][1]:
        max_square = max
#print(max_square)
#print(max_square[0])
#print(max_square[1])
#print(max_square[0][0])
#print(max_square[0][1])
#print(max_square[1][0])
#print(max_square[1][1])
#print(f'Максимально удаленная планета:  max_square[1][0]  с орбитой:  max_square[0]  и площадью:  max_square[1][1]')
print(f'Максимально удаленная планета: {max_square[1][0]} с орбитой: {max_square[0]} и площадью: {max_square[1][1]}')






