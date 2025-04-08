from Caballo.Launcher import Launcher as CaballoLauncher
from Reinas.Launcher import Launcher as ReinasLauncher

def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Ejecutar simulación del caballo")
    print("2. Ejecutar simulación de las reinas")
    print("3. Salir")

def main():
    print("Bienvenido al programa de simulaciones")
    while True:
        mostrar_menu()
        opcion = input("Ingrese su elección: ")
        
        if opcion == "1":
            CaballoLauncher.main(self=CaballoLauncher())
        elif opcion == "2":
                n = int(input("Introduce el tamaño del tablero (N): "))
                n_reinas = ReinasLauncher(n)
                n_reinas.main()
                ReinasLauncher.main()
        elif opcion == "3":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")