import pytest
from src.models.silla import Silla

def test_creacion_silla():
    silla = Silla(material="Madera", precio=50, tipo="Oficina")
    assert silla.material == "Madera"
    assert silla.precio == 50
    assert silla.tipo == "Oficina"
