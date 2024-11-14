import os
import sqlite3

class Product:
    def __init__(self, id=0, name = '', stock = 0, price = 0.0, status = 1):
        self.id = id
        self.name = name
        self.__stock = stock
        self.price = price
        self.__status = status

    def register_product(self):
        self.id = int(input("Ingresar ID del Producto: "))
        self.name = input("Ingresar Nombre del Producto: ")
        self.stock = int(input("Ingresar Stock: "))
        self.price = float(input("Ingresar Precio Unitario: "))

    def find_id(self, search_id, list_product):
        status = False
        for obj_product in list_product:
            if obj_product.id == search_id:
                status = True
                break
        return status

    def find_product(self, list_product):
        print("+----------Buscar Producto----------+")
        search_id = int(input("Ingresar ID del Producto: "))
        for obj_product in list_product:
            if obj_product.status == 1:
                if obj_product.id == search_id:
                    print(f"ID: {obj_product.id}\nNombre: {obj_product.name}\nStock: {obj_product.stock}\nPrecio Unitario: {obj_product.price}")
                    print("+-----------------------------------+")
                    return
        print("⛔ Producto no encontrado")

    def list_products(self, list_product):
        print("+------------ Lista de Productos ------------+")
        if len(list_product) != 0:
                for obj_product in list_product:
                    print(f"ID: {obj_product.id}\nNombre: {obj_product.name}\nStock: {obj_product.stock}\nPrecio Unitario: {obj_product.price}")
                    print("+--------------------------------------------+")
        else: 
            print("⛔ Lista vacía")
            print("+--------------------------------------------+")

    @property
    def stock(self):
        return self.__stock
    
    @stock.setter
    def stock(self, new_stock):
        self.__stock = new_stock

    def set_stock(self, list_product):
        print("+--------------------------------------------+")
        print("ACTUALIZAR STOCK 📝")
        search_id = int(input("Ingresar ID del Producto a modificar: "))
        find = self.find_id(search_id, list_product)
        if find == True:
            for obj_product in list_product:
                if obj_product.id == search_id:
                    print(f"Nombre: {obj_product.name}\nStock: {obj_product.stock}")
                    print("+--------------------------------------------+")
        else:
            print("⛔ Producto no encontrado")
            return 
        new_stock = int(input("Ingresar el nuevo stock: "))
        os.system('cls')
        for obj_product in list_product:
            if obj_product.id == search_id:
                obj_product.stock = new_stock
                print("+--------------------------------------------+")
                print("STOCK ACTUALIZADO ✅")
                print(f"ID: {obj_product.id}\nNombre: {obj_product.name}\nStock: {obj_product.stock}\nPrecio Unitario: {obj_product.price}")
                print("+--------------------------------------------+")
                return
            
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, new_status):
        self.__status = new_status

    #BORRADO LOGICO MEDIANTE SETTER
    def set_status(self, list_product):
        search_id = int(input("Ingresar ID del Producto a Eliminar: "))
        for obj_product in list_product:
            if obj_product.id == search_id:
                print(f"Nombre: {obj_product.name}\nEstado: {obj_product.status}")
        new_status = int(input("Ingresar el nuevo estado (0: Eliminar - 1: Reactivar): "))
        for obj_product in list_product:
            if obj_product.id == search_id:
                obj_product.status = new_status
                print(f"ID: {obj_product.id}\nNombre: {obj_product.name}\nStock: {obj_product.stock}\nPrecio Unitario: {obj_product.price}")
                return
    
    #BORRADO FISICO MEDIANTE ".remove()"     
    def delete_product(self, list_product):
        print("+--------------------------------------------+")
        print("ELIMINAR PRODUCTO 🛑")
        search_id = int(input("Ingresar ID del Producto a Eliminar: "))
        find = self.find_id(search_id, list_product)

        if find == True:
            for obj_product in list_product:
                if obj_product.id == search_id:
                    print(f"ID: {obj_product.id}\nNombre: {obj_product.name}")
                    print("+--------------------------------------------+")
                    add = 's'
                    while add != 'n':
                        add = input("Confirma ELIMINAR el producto? ('s': sí / 'n': no): ")
                        add_low = add.lower()
                        os.system('cls')
                        if add_low == 'n':
                            print("+--------------------------------------------+")
                            print("ELIMINAR PRODUCTO 🛑")
                            print("❎ Producto NO eliminado")
                            print("+--------------------------------------------+")
                            break
                        elif add_low == 's':
                            list_product.remove(obj_product)
                            print("+--------------------------------------------+")
                            print("ELIMINAR PRODUCTO 🛑")
                            print("✅ Producto Eliminado")
                            print("+--------------------------------------------+")
                            break
                        else:
                            print("+--------------------------------------------+")
                            print("ELIMINAR PRODUCTO 🛑")
                            input("Ingresar una opción válida!")
        else:
            print("⛔ Producto no encontrado")
            return

    def list_low_stock(self, list_product):
        low_stock = 0
        print("+------------ Lista de Stock Debajo de 10 ------------+")
        for obj_product in list_product:
            if obj_product.stock <  10:
                low_stock += 1
                print(f"ID: {obj_product.id}\nNombre: {obj_product.name}\nStock: {obj_product.stock}")
                print("+-----------------------------------------------------+")
        if low_stock == 0:
            print("No hay productos con stock bajo 😁")
            print("+-----------------------------------------------------+")