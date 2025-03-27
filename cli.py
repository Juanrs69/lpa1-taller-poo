import click
import json
from src.models.mesa import Mesa
from src.models.silla import Silla
from src.models.serializador import Serializador

@click.group()
def cli():
    "CLI para gestionar la mueblería"
    pass

@click.command()
@click.argument("material")
@click.argument("precio", type=float)
@click.argument("forma")
def agregar_mesa(material, precio, forma):
    "Agrega una nueva mesa al inventario"
    mesa = Mesa(material, precio, forma)
    guardar_mueble(mesa)
    click.echo(f"Mesa agregada: {mesa}")

@click.command()
@click.argument("material")
@click.argument("precio", type=float)
@click.argument("tipo")
@click.option("--respaldo", is_flag=True, help="Indica si la silla tiene respaldo")
def agregar_silla(material, precio, tipo, respaldo):
    "Agrega una nueva silla al inventario"
    silla = Silla(material, precio, tipo, respaldo)
    guardar_mueble(silla)
    click.echo(f"Silla agregada: {silla}")

@click.command()
def listar_muebles():
    "Lista todos los muebles en el inventario"
    muebles = Serializador.cargar_muebles("muebles.json")
    if not muebles:
        click.echo("No hay muebles en el inventario.")
    for mueble in muebles:
        click.echo(mueble)

@click.command()
@click.argument("indice", type=int)
def eliminar_mueble(indice):
    "Elimina un mueble del inventario por su índice"
    muebles = Serializador.cargar_muebles("muebles.json")
    if 0 <= indice < len(muebles):
        eliminado = muebles.pop(indice)
        Serializador.guardar_muebles(muebles, "muebles.json")
        click.echo(f"Mueble eliminado: {eliminado}")
    else:
        click.echo("Índice inválido.")

# Función auxiliar para guardar muebles
def guardar_mueble(mueble):
    try:
        muebles = Serializador.cargar_muebles("muebles.json")
    except (FileNotFoundError, json.JSONDecodeError):
        muebles = []
    muebles.append(mueble)
    Serializador.guardar_muebles(muebles, "muebles.json")

# Registrar los comandos
todo_cli = [agregar_mesa, agregar_silla, listar_muebles, eliminar_mueble]
for command in todo_cli:
    cli.add_command(command)

if __name__ == "__main__":
    cli()
