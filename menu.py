import os
class Menu:
    def __init__(self, option=-1):
        self.option = option
        
    def print_menu(self):
        try:
            print("+----------------MENU----------------+")
            print("|                                    |")
            print("|    1: Registrar Producto           |")
            print("|    2: Consulta de Productos        |")
            print("|    3: Actualizar Stock             |")
            print("|    4: Eliminar Producto            |")
            print("|    5: Listar Productos             |")
            print("|    6: Listar Stock Bajo            |")
            print("|    0: Salir                        |")
            print("|                                    |")
            print("+------------------------------------+")
            option = int(input("Ingresar opción: "))
            if option < 7:
                self.option = option
                return self.option
            else:
                print("❗ Ingresar una opción válida")
                print()
                input("Presiona una tecla para continuar...")
                self.option=-1 #resetea el valor de self.option
                os.system('cls')
            return self.option
        except Exception:
            print("❗ Ingresar una opción válida")
            print()
            input("Presiona una tecla para continuar...")
            self.option=-1
            os.system('cls')
            return
        
    def back_to_menu(self):
        print()
        input("Presiona una tecla para continuar...")
        os.system('cls')

    def exit(self):
        print("+------------------------------------+")
        print("|                                    |")
        print("| Gracias por utilizar la aplicación |")
        print("|              😀😁😉                |")
        print("|                                    |")
        print("+------------------------------------+")
        print()
        input("Presiona una tecla para continuar...")
        os.system('cls')