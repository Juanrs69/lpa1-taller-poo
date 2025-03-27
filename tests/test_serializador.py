import os
import json
from src.models.mesa import Mesa
from src.models.silla import Silla
from src.models.serializador import Serializador

def test_serializacion():
    muebles = [
        Mesa(material="Madera", precio=150, forma="Rectangular"),
        Silla(material="Metal", precio=50, tipo="Oficina"),
    ]
    archivo = "muebles_test.json"

    Serializador.guardar_muebles(muebles, archivo)
    
    assert os.path.exists(archivo)

    with open(archivo, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    assert len(data) == 2
    assert data[0]["material"] == "Madera"
    assert data[1]["tipo"] == "Silla"

    # Probar la deserialización
    muebles_cargados = Serializador.cargar_muebles(archivo)
    assert len(muebles_cargados) == 2
    assert isinstance(muebles_cargados[0], Mesa)
    assert isinstance(muebles_cargados[1], Silla)
    assert muebles_cargados[0].material == "Madera"
    assert muebles_cargados[1].tipo == "Oficina"

    os.remove(archivo)
