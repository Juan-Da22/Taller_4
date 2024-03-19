class Empleado:
    def __init__(self, nombre, apellidos, dni, direccion, telefono, salario, supervisor=None):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.direccion = direccion
        self.telefono = telefono
        self.salario = salario
        self.supervisor = supervisor

    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellidos: {self.apellidos}")
        print(f"DNI: {self.dni}")
        print(f"Dirección: {self.direccion}")
        print(f"Teléfono: {self.telefono}")
        print(f"Salario: {self.salario}")
        if self.supervisor:
            print(f"Supervisor: {self.supervisor.nombre}")

    def cambiar_supervisor(self, nuevo_supervisor):
        self.supervisor = nuevo_supervisor

    def incrementar_salario(self, porcentaje):
        self.salario *= (1 + porcentaje / 100)


class Secretario(Empleado):
    def __init__(self, nombre, apellidos, dni, direccion, telefono, salario, despacho, numero_fax):
        super().__init__(nombre, apellidos, dni, direccion, telefono, salario)
        self.despacho = despacho
        self.numero_fax = numero_fax

    def imprimir(self):
        super().imprimir()
        print("Puesto: Secretario")

    def incrementar_salario(self, porcentaje):
        self.salario *= (1 + (porcentaje + 5) / 100)


class Vendedor(Empleado):
    def __init__(self, nombre, apellidos, dni, direccion, telefono, salario, coche_empresa, telefono_movil, area_venta, comision):
        super().__init__(nombre, apellidos, dni, direccion, telefono, salario)
        self.coche_empresa = coche_empresa
        self.telefono_movil = telefono_movil
        self.area_venta = area_venta
        self.clientes = []
        self.comision = comision

    def imprimir(self):
        super().imprimir()
        print("Puesto: Vendedor")

    def dar_alta_cliente(self, cliente):
        self.clientes.append(cliente)

    def dar_baja_cliente(self, cliente):
        if cliente in self.clientes:
            self.clientes.remove(cliente)

    def cambiar_coche(self, coche):
        self.coche_empresa = coche

    def incrementar_salario(self, porcentaje):
        self.salario *= (1 + (porcentaje + 10) / 100)


class JefeZona(Empleado):
    def __init__(self, nombre, apellidos, dni, direccion, telefono, salario, despacho, secretario, coche_empresa):
        super().__init__(nombre, apellidos, dni, direccion, telefono, salario)
        self.despacho = despacho
        self.secretario = secretario
        self.vendedores = []
        self.coche_empresa = coche_empresa

    def imprimir(self):
        super().imprimir()
        print("Puesto: Jefe de Zona")

    def cambiar_secretario(self, nuevo_secretario):
        self.secretario = nuevo_secretario

    def cambiar_coche(self, coche):
        self.coche_empresa = coche

    def dar_alta_vendedor(self, vendedor):
        self.vendedores.append(vendedor)

    def dar_baja_vendedor(self, vendedor):
        if vendedor in self.vendedores:
            self.vendedores.remove(vendedor)

    def incrementar_salario(self, porcentaje):
        self.salario *= (1 + (porcentaje + 20) / 100)


# Programa de prueba
if __name__ == "__main__":

    supervisor = JefeZona("Juan", "Perez", "12345678A", "Calle Mayor 1", "123456789", 50000, "Despacho 1", None, "Audi A4")
    secretario = Secretario("Ana", "Garcia", "98765432B", "Calle Menor 2", "987654321", 25000, "Despacho 2", "555-123456")
    vendedor = Vendedor("Pedro", "Lopez", "87654321C", "Calle Pequeña 3", "876543210", 30000, "Ford Focus", "666-987654", "Zona Norte", 0.05)

    secretario.cambiar_supervisor(supervisor)

    vendedor.cambiar_supervisor(supervisor)

    empleados = [supervisor, secretario, vendedor]
    for empleado in empleados:
        empleado.incrementar_salario(5)

    for empleado in empleados:
        empleado.imprimir()
        print()
