
""" SEGUNDA PARTE PYTHON """

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def presentation(self):
        return f"Hola! Soy {self.nombre} y tengo {self.edad} años"

    def __str__(self):
        return f"Hola! Soy {self.nombre} y tengo {self.edad} años"

class Trabajador(Persona):
    """ APARTADO 4) """
    def __init__(self, nombre, edad, departamento = 'Data', puesto = 'Analyst'):
        Persona.__init__(self,nombre,edad)
        self.departamento = departamento
        self.puesto = puesto

    def presentation(self):
        print(Persona.presentation(self),f"pertenezco al departamento: {self.departamento} y mi puesto es {self.puesto}")

    def __str__(self):
        return f"{Persona.__str__(self)} pertenezco al departamento: {self.departamento} y mi puesto es {self.puesto}"



""" APARTADO 4) """
nombre = 'Alberto'
trabajador = Trabajador(nombre, 20)
print("Presentation: ", type(trabajador))
trabajador.presentation()



