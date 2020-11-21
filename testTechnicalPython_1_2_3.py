
""" SEGUNDA PARTE PYTHON """

"""APARTADO 1) """
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def presentation(self):
        return f"Hola! Soy {self.nombre} y tengo {self.edad} años"

    def __str__(self):
        return f"Hola! Soy {self.nombre} y tengo {self.edad} años"

""" APARTADO 2) """
class Trabajador(Persona):
    def __init__(self, nombre, edad, departamento = 'Data', puesto = 'Analyst'):
        Persona.__init__(self,nombre,edad)
        self.departamento = departamento
        self.puesto = puesto

    def presentation(self):
        print(Persona.presentation(self),f"pertenezco al departamento: {self.departamento} y mi puesto es {self.puesto}")

    def __str__(self):
        return f"{Persona.__str__(self)} pertenezco al departamento: {self.departamento} y mi puesto es {self.puesto}"


nombre = 'Alberto'
persona_1 = Persona(nombre, 20)
print("Presentation: ", type(persona_1))
print(persona_1.presentation())


trabajador_1 = Trabajador(nombre, 20, "Big Data", "big data architecture developer")
#print("Presentation: ", type(trabajador_1))
# Opción 1
print("Opción 1: ")
trabajador_1.presentation()
# Opción 2
print("Opción 2: ")
print(trabajador_1)

""" APARTADO 3) 

la diferencia entre self.nombre y la variable llamada nombre, en la función
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

Nombre es la variable que entra como parámetro a la función y self.nombre es el atributo para la clase Persona.

"""




