suma = 0 

for i in range (4):
    
    while True:

            try:
             numero = float(input(f"Ingrese el numero{i + 1}:"))

             suma = suma + numero
             
             break
            except:

                print("Error, debe ingresar un numero valido")


print("La suma total es: ", suma)
