
print("Selecciona tu pedido")
print("1 - Pikachu Roll $4.500")
print("2 - Otaku Roll $5.000")
print("3 - Pulpo Venenoso Roll $5.200")
print("4 - Anguila Electrica Roll $4.800")

roll1 = int(input("Selecciona tu pedido: "))

total = 0
pikachu = 4500
otaku = 5000
pulpo = 5200
anguila = 4800

while roll1 >= 5 and roll1 <= 0:
    print("no contamos con mas pedidos")
    print("Selecciona tu pedido")
    print("1 - Pikachu Roll $4.500")
    print("2 - Otaku Roll $5.000")
    print("3 - Pulpo Venenoso Roll $5.200")
    print("4 - Anguila Electrica Roll $4.800")

    roll1 = int(input("Selecciona tu pedido: "))


if roll1 == 1:
       
    print("Pikachu Roll: $", pikachu)
    cantidad = int(input("Selecciona tu cantidad: "))
    while cantidad <= 0:
        print("Error, selecciona una cantidad valida")
        cantidad = int(input("Selecciona tu cantidad: "))
    else:
        print("tu cantidad: ", cantidad)
    total = pikachu * cantidad
if roll1 == 2:
       
    print("Otaku Roll: $", otaku)
    cantidad = int(input("Selecciona tu cantidad: "))
    while cantidad <= 0:
        print("Error, selecciona una cantidad valida")
        cantidad = int(input("Selecciona tu cantidad: "))
    else:
        print("tu cantidad: ", cantidad)
    total = otaku * cantidad
if roll1 == 3:
       
    print("Pulpo Venenoso Roll: $", pulpo)
    cantidad = int(input("Selecciona tu cantidad: "))
    while cantidad <= 0:
        print("Error, selecciona una cantidad valida")
        cantidad = int(input("Selecciona tu cantidad: "))
    else:
        print("tu cantidad: ", cantidad)
    total = pulpo * cantidad
if roll1 == 4:
       
    print("Anguila Electrica Roll: $", anguila)
    cantidad = int(input("Selecciona tu cantidad: "))
    while cantidad <= 0:
        print("Error, selecciona una cantidad valida")
        cantidad = int(input("Selecciona tu cantidad: "))
    else:
        print("tu cantidad: ", cantidad)
    total = anguila * cantidad




print("1 - Pikachu Roll $4.500")
print("2 - Otaku Roll $5.000")
print("3 - Pulpo Venenoso Roll $5.200")
print("4 - Anguila Electrica Roll $4.800")


opcion1 = (input("¿Deseas continuar con tu pedido o finalizarlo?(X/F)"))
 
if opcion1 == "x":
   print ("Gracias por tu compra esta es tu boleta")
   print (roll1, cantidad, total)