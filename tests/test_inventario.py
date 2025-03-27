import pytest
from src.models.mesa import Mesa
from src.models.silla import Silla
from src.models.armario import Armario
from src.models.inventario import Inventario

def test_agregar_mueble():
    inventario = Inventario()
    mesa = Mesa(material="Madera", precio=150, forma="Rectangular")
    
    inventario.agregar_mueble(mesa)
    
    assert mesa in inventario.muebles
    assert inventario.contar_muebles() == 1

def test_eliminar_mueble():
    inventario = Inventario()
    silla = Silla(material="Metal", precio=50, tipo="Oficina")

    inventario.agregar_mueble(silla)
    inventario.eliminar_mueble(silla)

    assert silla not in inventario.muebles
    assert inventario.contar_muebles() == 0

def test_listar_muebles():
    inventario = Inventario()
    armario = Armario(material="Plástico", precio=200, puertas=2)
    
    inventario.agregar_mueble(armario)
    
    lista_muebles = inventario.listar_muebles()
    
    assert len(lista_muebles) == 1
    assert "Armario" in lista_muebles[0]
