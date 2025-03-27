import pytest
from src.models.mesa import Mesa

def test_precio_final():
    mesa = Mesa(material="Metal", precio=100, forma="Redonda")
    mesa.aplicar_descuento(20)  # 20% de descuento

    # 🚀 Depuración
    print(f"Precio con descuento (Mesa): {mesa.precio}")
    print(f"Precio final calculado (Mesa): {mesa.calcular_precio_final()}")

    assert mesa.calcular_precio_final() == 92.0  # 80.0 + 15% = 92.0
