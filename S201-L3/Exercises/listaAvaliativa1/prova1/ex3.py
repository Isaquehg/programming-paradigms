def mod_array(array, n):
    for i in range(len(array)):
        array[i] *= n
        print(f"Posição {i}: {array[i]}")


n = int(input("Número a multiplicar: "))
array = []

cont = 30
for i in range(31):
    array.append(cont - i)

mod_array(array, n)