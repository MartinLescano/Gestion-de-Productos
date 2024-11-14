from menu import Menu
from product import Product
import os

os.system('cls')
obj_product = Product()
obj_menu = Menu()
list_product = []

#DICCIONARIO
def option_1():
    add = 'x'
    add_low = add
    while add != 'n':
        obj_product = Product()
        print("+--------------------------------------------+")
        print("REGISTRAR PRODUCTO 1📦")
        try:
            obj_product.register_product()
        except Exception as ex:
            print("#️⃣ Ingresar un ID válido.", type(ex))
            obj_menu.back_to_menu()
            break
        list_product.append(obj_product)
        add_low= 'x'
        while add_low != 's' and add_low != 'n':
            add = input("Registrar otro Producto? ('s': sí / 'n': no): ")
            add_low = add.lower()
            os.system('cls')
            if add_low == 'n':
                return
            elif add_low != 's':
                print("+--------------------------------------------+")
                print("REGISTRAR PRODUCTO 2📦")
                input("Ingresar una opción válida!")

def option_2():
    obj_product = Product()
    try:
        obj_product.find_product(list_product)
    except Exception as ex:
        print("#️⃣ Ingresar un ID válido.", type(ex))
    obj_menu.back_to_menu()

def option_3():
    obj_product = Product()
    try:
        obj_product.set_stock(list_product)
    except Exception as ex:
        print("#️⃣ Ingresar un ID válido.", type(ex))
    obj_menu.back_to_menu()  

def option_4():
    obj_product = Product()
    try:
        #obj_product.set_status(list_product) #Eliminación lógica
        obj_product.delete_product(list_product)
    except Exception as ex:
        print("#️⃣ Ingresar un ID válido.", type(ex))
    obj_menu.back_to_menu()

def option_5():
    obj_product.list_products(list_product)
    obj_menu.back_to_menu()

def option_6():
    obj_product.list_low_stock(list_product)
    obj_menu.back_to_menu()

def option_0():
    obj_menu.exit()

def invalid_option():
    return

switch = {
    1: option_1,
    2: option_2,
    3: option_3,
    4: option_4,
    5: option_5,
    6: option_6,
    0: option_0
}

#MENU
while True:
    obj_menu.print_menu()
    os.system('cls')

    function = switch.get(obj_menu.option, invalid_option)

    if obj_menu.option !=0:
        function()
    else:
        function()
        break