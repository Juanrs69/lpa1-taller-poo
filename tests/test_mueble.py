import pytest
from src.models.silla import Silla

def test_precio_negativo():
    with pytest.raises(ValueError):
        Silla(material="Madera", precio=-10, tipo="Oficina")
