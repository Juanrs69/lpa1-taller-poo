# Archivo principal
from rich.console import Console
from rich.table import Table
from models.silla import Silla
from models.mesa import Mesa
from models.armario import Armario

# Creamos una consola de Rich
console = Console()

def mostrar_muebles(muebles):
    """
    Muestra una tabla con información de los muebles.

    :param muebles: Lista de objetos de tipo Mueble.
    """
    table = Table(title="Inventario de Muebles")

    # Definimos las columnas de la tabla
    table.add_column("Tipo", style="cyan", justify="center")
    table.add_column("Material", style="magenta", justify="center")
    table.add_column("Precio Base ($)", style="yellow", justify="center")
    table.add_column("Precio Final ($)", style="green", justify="center")

    # Agregamos cada mueble a la tabla
    for mueble in muebles:
        table.add_row(
            mueble.__class__.__name__,  # Tipo de mueble (Silla, Mesa, Armario)
            mueble.material,
            f"{mueble.precio:.2f}",
            f"{mueble.calcular_precio_final():.2f}"
        )

    console.print(table)

# Crear instancias de muebles
silla1 = Silla(material="Madera", precio=50.0, tiene_respaldo=True)
silla2 = Silla(material="Plástico", precio=30.0, tiene_respaldo=False)

mesa1 = Mesa(material="Mármol", precio=200.0, forma="Redonda")
mesa2 = Mesa(material="Madera", precio=150.0, forma="Cuadrada")

armario1 = Armario(material="Metal", precio=300.0, num_puertas=2)
armario2 = Armario(material="Madera", precio=250.0, num_puertas=3)

# Lista de muebles
muebles = [silla1, silla2, mesa1, mesa2, armario1, armario2]

# Mostrar la tabla con los muebles
mostrar_muebles(muebles)


