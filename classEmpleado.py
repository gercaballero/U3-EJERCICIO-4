
class Empleado:
    __nombre=''
    __dni=''
    __direccion=''
    __telefono=''

    def __init__(self,nombre,dni,direccion,tel):
        self.__nombre=nombre
        self.__dni=dni
        self.__direccion=direccion
        self.__telefono=tel
        
    def __str__(self):
        return ('Nombre:{:20}\tDNI:{}\tDIRECCION:{:15}\tTEL:{}'.format(self.__nombre,self.__dni,self.__direccion,self.__telefono))
    def getDni(self):
        return self.__dni
    def getNombre(self):
        return self.__nombre
    def getDireccion(self):
        return self.__direccion
    def getTelefono(self):
        return self.__telefono
    
        