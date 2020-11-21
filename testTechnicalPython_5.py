
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
    def __init__(self, list):
        Persona.__init__(self, list[0], list[1])
        self.departamento = list[2]
        self.puesto = list[3]

    def presentation(self):
        print(Persona.presentation(self),f"pertenezco al departamento: {self.departamento} y mi puesto es {self.puesto}")

    def __str__(self):
        return f"{Persona.__str__(self)} pertenezco al departamento: {self.departamento} y mi puesto es {self.puesto}"


""" APARTADO 5) """
my_var_list = [ 'Andrea', '42', 'Ventas', 'Manager']
for v in my_var_list:
    print(v)

trabajador_2 = Trabajador(my_var_list)
trabajador_2.presentation()


