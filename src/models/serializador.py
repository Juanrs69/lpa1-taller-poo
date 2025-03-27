import json
from src.models.mesa import Mesa
from src.models.silla import Silla

class Serializador:
    @staticmethod
    def guardar_muebles(muebles, archivo):
        """Guarda una lista de muebles en un archivo JSON."""
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump([mueble.to_dict() for mueble in muebles], f, indent=4)

    @staticmethod
    def cargar_muebles(archivo):
        """Carga una lista de muebles desde un archivo JSON y los convierte en objetos."""
        with open(archivo, "r", encoding="utf-8") as f:
            data = json.load(f)

        muebles = []
        for item in data:
            if item["tipo"] == "Mesa":
                muebles.append(Mesa(item["material"], item["precio"], item["forma"]))
            elif item["tipo"] == "Silla":
                muebles.append(Silla(item["material"], item["precio"], item["tipo_silla"], item.get("tiene_respaldo", False)))

        return muebles
