lista = [1,2,3,4,5,6,7,8,9]

suma = 0
for item in lista:
    suma = suma + item
    
print("El valor de item es: " + str(suma))

listaVariable = [1,"A",23,"C","Hola",45.3]

valorHola= listaVariable[4]
print(valorHola)

valorAencontrar = input("Que numero del cliente desea buscar ")

numeros = [124,243,4234,3552,3422,241,3423]

for n in numeros:
    if n == int(valorAencontrar):
        print("El cliente existe")
        break
    else:
      print('No se a encontrado el cliente')