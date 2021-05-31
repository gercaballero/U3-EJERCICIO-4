from classEmpleado import Empleado
class EmpleadoExterno(Empleado):
    __tarea=None
    __fechaInicio=None
    __fechaFinalizacion=None
    __montoViatico=0.0
    __costoObra=0.0
    __montoSeguro=0.0
    
    def __init__(self, nombre, dni, direccion, tel,tarea,finicio,ffinal,montoV,costoO,montoS):
        super().__init__(nombre, dni, direccion, tel)
        self.__tarea=tarea
        self.__fechaInicio=finicio
        self.__fechaFinalizacion=ffinal
        self.__montoViatico=montoV
        self.__costoObra=costoO
        self.__montoSeguro=montoS
    
    def __str__(self):
        return('{}\tTarea:{}\tCostoObra:{}'.format(super().__str__(),self.__tarea,self.__costoObra))
    def getTarea(self):
        return self.__tarea
    def getCostoObra(self):
        return float(self.__costoObra)
    
    def sueldo(self):
        return float(self.__costoObra-self.__montoViatico-self.__montoSeguro)
    def getNombre(self):
        return super().getNombre()
