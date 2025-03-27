import pytest
from src.models.armario import Armario

def test_creacion_armario():
    armario = Armario(material="Plástico", precio=150, puertas=2)
    assert armario.material == "Plástico"
    assert armario.precio == 150
    assert armario.puertas == 2
