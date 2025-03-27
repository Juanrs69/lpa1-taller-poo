from src.models.mueble import Mueble

class Inventario:
    """
    Clase para gestionar el inventario de la mueblería.
    """

    def __init__(self):
        self.muebles = []

    def agregar_mueble(self, mueble: Mueble):
        """
        Agrega un mueble al inventario.
        :param mueble: Objeto de tipo Mueble o sus subclases.
        """
        if not isinstance(mueble, Mueble):
            raise TypeError("Solo se pueden agregar objetos de tipo Mueble")
        self.muebles.append(mueble)

    def eliminar_mueble(self, mueble: Mueble):
        """
        Elimina un mueble del inventario si existe.
        :param mueble: Objeto de tipo Mueble o sus subclases.
        """
        if mueble in self.muebles:
            self.muebles.remove(mueble)

    def listar_muebles(self):
        """
        Devuelve una lista con la representación en cadena de todos los muebles en el inventario.
        """
        return [str(mueble) for mueble in self.muebles]

    def contar_muebles(self):
        """
        Devuelve el número total de muebles en el inventario.
        """
        return len(self.muebles)
