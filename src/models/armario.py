from .mueble import Mueble  # Importamos la clase base Mueble

class Armario(Mueble):
    """
    Representa un armario, heredando de Mueble.
    """

    def __init__(self, material: str, precio: float, puertas: int):  # Cambié num_puertas -> puertas
        """
        Constructor de la clase Armario.

        :param material: Material del armario.
        :param precio: Precio base del armario.
        :param puertas: Número de puertas del armario.
        """
        super().__init__(material, precio)
        self.puertas = puertas  # Cambié self.num_puertas -> self.puertas

    def calcular_precio_final(self) -> float:
        """
        Calcula el precio final del armario.
        Cada puerta adicional aumenta el precio en un 5%.
        """
        return self.precio * (1 + (self.puertas - 1) * 0.05)  # Cambié self.num_puertas -> self.puertas

    def __str__(self):
        """
        Representación en cadena del armario.
        """
        return f"Armario de {self.puertas} puertas, Material: {self.material}, Precio Final: ${self.calcular_precio_final():.2f}"
