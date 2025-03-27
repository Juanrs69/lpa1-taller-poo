from abc import ABC, abstractmethod  # Importamos ABC para clases abstractas
from abc import ABC, abstractmethod

class Mueble(ABC):
    """
    Clase abstracta que representa un mueble genérico.
    Define atributos comunes como material y precio,
    y un método abstracto para calcular el precio final.
    """

    def __init__(self, material: str, precio: float):
        """
        Constructor de la clase Mueble.

        :param material: Material del mueble (ejemplo: madera, metal).
        :param precio: Precio base del mueble en dólares.
        :raises ValueError: Si el material es inválido o el precio es negativo.
        """
        if not isinstance(material, str) or not material.strip():
            raise ValueError("El material debe ser una cadena no vacía")  # 🚀 Evita materiales inválidos
        
        if not isinstance(precio, (int, float)) or precio < 0:
            raise ValueError("El precio no puede ser negativo")  # 🚀 Evita precios negativos
        
        self.material = material.strip()
        self.precio = precio

    @abstractmethod
    def calcular_precio_final(self) -> float:
        """
        Método abstracto para calcular el precio final del mueble.
        Debe ser implementado por las subclases.
        """
        pass

    def aplicar_descuento(self, porcentaje: float):
        """
        Aplica un descuento al precio del mueble.

        :param porcentaje: Porcentaje de descuento (entre 0 y 100).
        :raises ValueError: Si el porcentaje no está en el rango válido.
        """
        if not isinstance(porcentaje, (int, float)) or not (0 <= porcentaje <= 100):
            raise ValueError("El descuento debe estar entre 0 y 100")  # 🚀 Evita valores inválidos
        
        self.precio -= self.precio * (porcentaje / 100)

    def to_dict(self):
        """
        Convierte el objeto a un diccionario para serialización JSON.
        """
        return {
            "tipo": self.__class__.__name__,
            "material": self.material,
            "precio": self.precio
        }

    def __str__(self):
        """
        Representación en cadena del mueble.
        """
        return f"Mueble de {self.material}, Precio: ${self.precio:.2f}"