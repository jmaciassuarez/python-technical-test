
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
    def __init__(self, dictionary):
        for k, v in dictionary.items():
             setattr(self, k, v)

    def presentation(self):
        print(Persona.presentation(self),f"pertenezco al departamento: {self.departamento} y mi puesto es {self.puesto}")

    def __str__(self):
        return f"{Persona.__str__(self)} pertenezco al departamento: {self.departamento} y mi puesto es {self.puesto}"


""" APARTADO 6) """
my_var_dict = { 'nombre': 'Andrea', 'edad': '42', 'departamento': 'Ventas' , 'puesto': 'Manager'}
trabajador_3 = Trabajador(my_var_dict)
trabajador_3.presentation()



