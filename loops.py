# Media


data_set = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [10, 11, 12],
            [13, 14, 15]]

# Realizar la media de los ultimos valores 
suma = 0
for i in data_set:
    suma += i[-1]
    
media = suma / len(data_set)

# print(media)

# Ejercicio 1

# Ejercicio: escribe un programa que imprima todos los números menores de 50 que son múltiplos de 7

for i in range(1, 51):
    if i % 7 == 0:
        print(i)
        
# Ejercicio: crea una lista y añade a ella sólo los números negativos que aparecen en posición par (0, 2, 4...) de la lista original

nums = [5, -12, 66, 34, -1, 100, -8]

nums_neg = []

for i in range(len(nums)):
    if i % 2 == 0 and nums[i] < 0:
        nums_neg.append(nums[i])
        
print(nums_neg)

# Número menores a 50

for number in range(50):
    print(number)