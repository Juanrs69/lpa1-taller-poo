from .mueble import Mueble  

class Mesa(Mueble):
    """ Representa una mesa, heredando de Mueble. """

    def __init__(self, material: str, precio: float, forma: str):
        """ Constructor de la clase Mesa. """
        super().__init__(material, precio)
        self.forma = forma

    def calcular_precio_final(self) -> float:
        """ Calcula el precio final de la mesa después de aplicar descuentos. """
        precio_base = self.precio  # Ya tiene el descuento aplicado
        if self.forma.lower() == "redonda":
            precio_base *= 1.15  # Aplica el 15% adicional
        return round(precio_base, 2)  # Redondear para evitar errores de precisión
    
    def to_dict(self):
        """Convierte el objeto a un diccionario para serialización JSON"""
        return {
            "tipo": self.__class__.__name__,
            "material": self.material,
            "precio": self.precio,
            "forma": self.forma
        }
