from classEmpleado import Empleado
class EmpleadoContratado(Empleado):
    __fechaInicio=''
    __fechaFinal=''
    __cantHoras=0
    valorHora=10
    
    def __init__(self, nombre, dni, direccion, tel, finicio,ffinal,cantHoras):
        super().__init__(nombre, dni, direccion, tel)
        self.__fechaInicio=finicio
        self.__fechaFinal=ffinal
        self.__cantHoras=cantHoras
    def __str__(self):
        return ('{}\tcantHoras:{}'.format(super().__str__(),self.__cantHoras))
    def acumHoras(self,horas):
        if isinstance(horas, int):
            self.__cantHoras+=horas
    def sueldo(self):
        return float(self.__cantHoras*EmpleadoContratado.valorHora)
    def getNombre(self):
        return super().getNombre()