#Voy a hacer un software para una tienda electronica, donde puedas ingresar como comprador o como empleado
#y cada uno va  tener sus distintas opciones, logicamente se va a necesitar un inicio de sesion para ser empleado

from Funciones import *
exit = 0

while exit == 0:
    exit1 = 0
    print('________________________________________________\n'
          '|             TIENDA ELECTRONICA                |\n'
          '________________________________________________')
    print('')
    usuario = int(input('Buenos Dias, De que forma quiere ingresar?\n'
                        '1- Comprador\n'
                        '2- Empleado\n'
                        '3- Salir\n'
                        '> '))

    if usuario == 1:
        login = 1
    elif usuario == 2:
        login = 2
    elif usuario == 3:
        login = 3

    while exit1 == 0:
        if login == 1:
            print('')
            menu = int(input('Menu Usuario:\n'
                             '1- Componentes de Computadoras\n'
                             '2- Notebooks\n'
                             '3- Computadoras pre-armadas\n'
                             '4- Cerrar Sesion\n'
                             '> '))

            if menu == 1:
                Comprar(1)

            elif menu == 2:
                Comprar(2)

            elif menu == 3:
                Comprar(3)



            elif menu == 4:
                exit1 = 1


        elif login == 2:

            contrasenia = 'PEPE123'
            intentos = 0
            access = 0
            while intentos <= 3:
                intento = input('Ingrese la contrasenia:\n> ')
                if intento == contrasenia:
                    print('\nACCESO PERMITIDO\n')
                    access = 1
                    break
                else:
                    print('\nACCESO DENEGADO, INTENTE DE NUEVO\n')
                    intentos += 1
                    access = 0

            if intentos == 3:
                print('\nLIMITE DE INGRESOS ALCANZADO\n')

            while access == 1:
                print('')
                menu1 = int(input('Menu Empleado:\n'
                                  '1- Agregar algun producto\n'
                                  '2- Cambiar estock\n'
                                  '3- Cambiar precio\n'
                                  '4- Cerrar sesion\n'
                                  '> '))

                if menu1 == 1:
                    print('')
                    menu2 = int(input('Que desea agregar?\n'
                                      '1- Computadora \n'
                                      '2- Componente \n'
                                      '3- Notebook \n'
                                      '> '))

                    if menu2 == 1:
                        Agregarcomputadora()
                    elif menu2 == 2:
                        AgregarComponente()
                    elif menu2 == 3:
                        Agregarnotebook()

                elif menu1 == 2:
                    Cambiar_stock()

                elif menu1 == 3:
                    Cambiar_Precio()

                elif menu1 == 4:
                    exit1 = 1
                    break


        elif login == 3:
            exit1 = 1
            exit = 1