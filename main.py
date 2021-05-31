from classColeccion import Coleccion
from menu import Menu
import os
if __name__=='__main__':
    dimension=10
    co=Coleccion(dimension)
    co.test('planta.csv')
    co.test('contratados.csv')
    co.test('externos.csv')
    #co.listar()
    #input() 
    menu= Menu()
    salir= False     
    os.system('cls')      
    while not salir:
            print("-------------------Menu-------------------")
            print(' 1- REGISTRAR HORAS')
            print(' 2- TOTAL TAREA')
            print(' 3- AYUDA')
            print(' 4- CALCULAR SUELDO')
            print(' 5- SALIR')
            op= input('\n INGRESE UNA OPCION: ')
            if op in ('1','2','3','4','5'):
                menu.opcion(int(op),co)
                if op=='5':
                    salir=True
            else:
                os.system('cls')
                print ("---OPCION NO VALIDA---")
            input()
            os.system('cls')