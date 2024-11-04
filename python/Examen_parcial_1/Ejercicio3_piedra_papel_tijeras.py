from random import randint

print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 28  octubre del 2024                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" *  Ejercicio3_piedra_papel_tijeras.py                              * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")


'''
Este programa es el famoso juego de "piedra, papel o tijera", en donde el contrincante es la CPU. 
La opción de la CPU se escogerá de forma aleatorio con la función randint().
El juego mostrará las victorias del jugador, los partidos empatados y las victorias del CPU. 
Además, mostrará el siguiente menú:
1) Piedra.
2) Papel.
3) Tijera.
0) Salir.
Cualquier otro caso -> Mostrar un mensaje de "opción no válida".
Para ello:
a) Muestre la cantidad de victorias, empates y derrotas.
b) Pida al usuario una opción del menú.
c) Realice la lógica adecuada para calcular al ganador.
d) Muestre en la consola la elección del jugador, del CPU y el resultado.
e) Repita nuevamente el menú hasta salir.
'''
opcion = 1
puntos_usuario, puntos_cpu, empate = 0,0,0
while opcion != 0:
    print(" ")
    print(" ")
    print(f"Victorias jugador = {puntos_usuario} || Empates = {empate} || Victorias CPU = {puntos_cpu} ")
    print(" ** ¿Piedra papel o tijera?**  ")
    print("1) Piedra. ")
    print("2) Papel. ")
    print("3) Tijera. ")
    print("0) Salir.")
    opcion = int(input("ingrese una opción: "))
    opcion_cpu = randint(1,3)

    if (opcion == 1 and opcion_cpu == 3 ) or (opcion == 2 and opcion_cpu == 1) or (opcion == 3 and opcion_cpu == 2): #punto para el usuario
        puntos_usuario += 1
        print(f" CPU eligió:     {opcion_cpu}")
        print("Usuario gana")
    elif (opcion == 1 and opcion_cpu == 2 ) or (opcion == 2 and opcion_cpu == 3) or (opcion == 3 and opcion_cpu == 1):#punto para cpu
        puntos_cpu += 1
        print(f" CPU eligió:     {opcion_cpu}")
        print("CPU gana")
    elif opcion == opcion_cpu:
        empate += 1
        print(f" CPU eligió:     {opcion_cpu}")
        print("Empate")
    elif opcion == 0:
        print("FIN DEL JUEGO")
        print("PUNTOS TOTALES")
        print(f"Victorias jugador = {puntos_usuario} || Empates = {empate} || Victorias CPU = {puntos_cpu} ")