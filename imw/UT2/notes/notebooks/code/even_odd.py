# ===================== IMPORTS =====================================
import crayons


# ===================== FUNCIONES ===================================
def is_even(n):
    if n % 2:
        return False
    else:
        return True


def read_int():
    x = input('Introduzca un número entero: ')
    return int(x)


def menu():
    exit = False
    while not exit:
        print('''
        1. Chequear si un número es par ó impar.
        2. Salir.
        ''')
        option = input('')
        if option == '1':
            v = read_int()
            if is_even(v):
                print(crayons.green('El número es par!'))
            else:
                print(crayons.magenta('El número es impar!'))
        elif option == '2':
            print('👋🏻  Hasta luego Lucas!')
            exit = True
        else:
            print(crayons.red('La opción elegida no existe!'))


# ===================== CÓDIGO ======================================
if __name__ == '__main__':
    menu()
