print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 28  octubre del 2024                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" *  Ejercicio1_lic_Informática                                      * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")


'''
Este programa imprime en consola los números, separados por comas, del 1 hasta un número ingresado por el usuario.
Sin embargo, se deben sustituir los siguientes valores:
3 o sus múltiplos por la palabra "Licenciatura".
5 y sus múltiplos por la palabra "Informática".
Múltiplos de 3 y 5 por la frase "Licenciatura en Informática" y se imprima un salto de línea en lugar de la coma.
Para ello:
a) Solicite un número en consola.
b) Realizar la lógica adecuada para imprimir los números o mensajes adecuados.
c) Mostrar los resultados en consola.
'''

numero_final=int(input("ingrese el número al final de la cuenta: "))
contador = 0
while contador <= numero_final:
    if contador % 3 == 0 and contador  % 5 == 0:
        print("Licenciatura en Informática")
    elif contador % 3 == 0:
        print(f"Licenciatura ,", end=" ")
    elif contador % 5 == 0:
        print(f"Informática, ", end=" ")
    else :
        print(f"{contador}, ", end=" ")
    contador+=1