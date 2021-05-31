import os
from classColeccion import Coleccion
class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            4:self.opcion4,
                            5:self.salir
                         }
    def getSwitcher(self):
        return self.__switcher
    def opcion(self,op,co):
        func= self.__switcher.get(op, lambda: print("Opción no válida"))
        func(co)

    def salir(self,co):
        print('Salida del programa')

    def opcion1(self,co):
        os.system('cls')
        print('---------REGISTRO DE HORAS---------')
        dni=input('INGRESE EL DNI DEL EMPLEADO:')
        band=False
        while not band:
            indice=co.buscarIndice(dni)
            if indice!=False:
                os.system('cls')
                print('---------REGISTRO DE HORAS---------')
                horas=input('CANTIDAD DE HORAS TRABAJADAS HOY POR DNI:{}: '.format(dni))
                co.agregarHoras(int(horas),indice)
                print('\n++++++ SE LE AGREGARON {} HORAS AL EMPLEADO CON DNI:{}++++++'.format(horas,dni))
                band=True
                input()
                os.system('cls')
            else:
                os.system('cls')
                print('---------REGISTRO DE HORAS---------')
                print('DNI NO SE ENCUENTRA O NO ES CONTRATADO. REINTENTE')
                dni=input('INGRESE EL DNI DEL EMPLEADO:')
        co.listar()
        input()
        os.system('cls')
        
    def opcion2(self,co):
        band=False
        print('---------MONTO POR TAREA---------')
        tarea=input('INGRESE TAREA:')
        while not band:
            if tarea in ('carpinteria','electricidad','plomeria'):
                os.system('cls')
                print('---------MONTO POR TAREA---------')
                print ('EL TOTAL DE LA TAREA {} ES DE {}'.format(tarea.upper(),co.totalTarea(tarea)))
                band=True
            else:
                os.system('cls')
                print('---------MONTO POR TAREA---------')
                print('TAREA INCORRECTA. REINTENTE\n')
                tarea=input('INGRESE TAREA:')
        input()
        os.system('cls')
    def opcion3(self,co):
        os.system('cls')
        print('\t\t~~~LISTA DE AYUDADOS POR LA EMPRESA~~~')
        co.listarAyudados()
        
    def opcion4(self,co):
        os.system('cls')
        print('\t\t~~~~~~SUELDOS EMPLEADOS~~~~~~')
        co.ListarSueldos()
        input()
        os.system('cls')