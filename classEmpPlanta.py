from classEmpleado import Empleado
class EmpleadoPlanta(Empleado):
    __sueldoBasico=0.0
    __antiguedad=0
    
    def __init__(self, nombre, dni, direccion, tel,sueldo,antiguedad):
        super().__init__(nombre, dni, direccion, tel)
        self.__sueldoBasico=sueldo
        self.__antiguedad
    
    def __str__(self):
        return('{}\tSueldo:{}\tAntiguedad:{}'.format(super().__str__(),self.__sueldoBasico,self.__antiguedad))
    
    def sueldo(self):
        return float(self.__sueldoBasico+(self.__sueldoBasico*0.01*self.__antiguedad))
    def getNombre(self):
        return super().getNombre()