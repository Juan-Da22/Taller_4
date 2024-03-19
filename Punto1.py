class Vehiculo:
    def __init__(self, matricula):
        self.matricula = matricula
        self.velocidad = 0
    
    def acelerar(self, cantidad):
        self.velocidad += cantidad
    
    def __str__(self):
        return f"Matrícula: {self.matricula}, Velocidad: {self.velocidad} km/h"

class Coche(Vehiculo):
    def __init__(self, matricula, num_puertas):
        super().__init__(matricula)
        self.num_puertas = num_puertas
    
    def obtener_num_puertas(self):
        return self.num_puertas

class Camion(Vehiculo):
    def __init__(self, matricula):
        super().__init__(matricula)
        self.remolque = None
    
    def poner_remolque(self, remolque):
        self.remolque = remolque
    
    def quitar_remolque(self):
        self.remolque = None
    
    def acelerar(self, cantidad):
        if self.remolque and (self.velocidad + cantidad) > 100:
            raise DemasiadoRapidoException("El camión con remolque no puede superar los 100 km/h")
        else:
            self.velocidad += cantidad
    
    def __str__(self):
        if self.remolque:
            return f"Matrícula: {self.matricula}, Velocidad: {self.velocidad} km/h, Remolque: {self.remolque}"
        else:
            return f"Matrícula: {self.matricula}, Velocidad: {self.velocidad} km/h"

class Remolque:
    def __init__(self, peso):
        self.peso = peso
    
    def __str__(self):
        return f"Remolque - Peso: {self.peso} kg"

class DemasiadoRapidoException(Exception):
    pass
