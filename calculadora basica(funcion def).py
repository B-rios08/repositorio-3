def suma (a,b):
    return a + b

def resta (a,b):
    return a - b

def multiplicacion (a,b):
    return a * b

def division (a,b):
    if b == 0:
        
        return "Error, no se puede dividir por cero"
        
    return a / b

print("=========|| CALCULADORA ||=========")


num1 = float (input("Ingresa tu primero numero: "))


num2 = float (input("Ingresa tu segundo numero: "))

print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("Selecciona tu operacion: ")

if opcion == "1":
    
    print("Resultado: ", suma(num1, num2))


elif opcion == "2":

    print("Resultado: ", resta(num1, num2))


elif opcion == "3":

    print("Resultado: ", multiplicacion(num1, num2))


elif opcion == "4":

    print("Resultado: ", division(num1, num2))

else:
    print("Error opcion invalida")    