print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 28  octubre del 2024                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" *  Ejercicio2_area_perimetro.py                                    * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")

'''
Este programa determina el área y el perímetro de un rectángulo o de un círculo.
Muestre el siguiente menú:

1) Calcular el área de un rectángulo.
2) Calcular el perímetro de un rectángulo.
3) Calcular el área de un círculo.
4) Calcular el perímetro de un círculo.
0) Salir.
Cualquier otro caso -> Mostrar un mensaje de "opción no válida".
Para ello:
a) Muestre el menú anterior en consola.
b) En caso de calcular un área o perímetro, solicite al usuario los valores requeridos (flotantes).
c) Utilice la lógica adecuada para calcular lo solicitado. Asuma pi = 3.1416.
d) Imprima el resultado en la consola. Nota: muestre únicamente 3 decimales en todos los casos.
e) Repita el menú hasta salir.
'''
pi = 3.1416
opcion = 1
while opcion != 0:
    print(" ")
    print("** programa que calcula área y perímetro **")
    print("1) Calcular el área de un rectángulo. ")
    print("2) Calcular el perímetro de un rectángulo. ")
    print("3) Calcular el área de un círculo. ")
    print("4) Calcular el perímetro de un círculo.")
    print("0) Salir. ")
    opcion = int(input("ingrese una opción: "))

    if opcion == 1:
        base, altura = float(input("ingrese medida base en cm: ")), float(input("ingrese medida de la altura en cm: "))
        print(f"El área del rectángulo es de {(base * altura):.3f} cm")
    elif opcion == 2:
        base, altura = float(input("ingrese medida base en cm: ")), float(input("ingrese medida de la altura en cm"))
        print(f"El perímetro del rectángulo es de {((base * 2) + (altura * 2)):.3f} cm")
    elif opcion == 3:
        radio = float(input("ingrese radio del círculo en cm: "))
        print(f"El área del círculo es de {(pi * (radio * radio)):.3f} cm")
    elif opcion == 4:
        radio = float(input("ingrese radio del círculo en cm: "))
        print(f"El perímetro del círculo es de {(2 * pi * radio):.3f} cm")
    elif opcion == 0:
        print("saliendo del programa...")
    else:
        print("Opción no válida :( ")