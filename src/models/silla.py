from .mueble import Mueble

class Silla(Mueble):
    """
    Representa una silla, heredando de Mueble.
    """

    def __init__(self, material: str, precio: float, tipo: str, tiene_respaldo: bool = False):
        """
        Constructor de la clase Silla.

        :param material: Material de la silla.
        :param precio: Precio base de la silla.
        :param tipo: Tipo de silla (ejemplo: oficina, comedor).
        :param tiene_respaldo: Indica si la silla tiene respaldo (por defecto es False).
        """
        super().__init__(material, precio)
        self.tipo = tipo
        self.tiene_respaldo = tiene_respaldo

    def calcular_precio_final(self) -> float:
        """Calcula el precio final de la silla."""
        return self.precio * 1.10 if self.tiene_respaldo else self.precio

    def to_dict(self):
        """Convierte el objeto Silla a un diccionario para serialización JSON."""
        return {
            "tipo": "Silla",  # Se asegura de que siempre diga "Silla"
            "material": self.material,
            "precio": self.precio,
            "tipo_silla": self.tipo,  # Renombramos la clave para evitar conflicto
            "tiene_respaldo": self.tiene_respaldo
        }

    def __str__(self):
        """Representación en cadena de la silla."""
        respaldo = "con respaldo" if self.tiene_respaldo else "sin respaldo"
        return f"Silla {self.tipo} {respaldo}, Material: {self.material}, Precio Final: ${self.calcular_precio_final():.2f}"
