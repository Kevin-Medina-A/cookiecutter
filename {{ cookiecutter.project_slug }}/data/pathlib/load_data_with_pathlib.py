from pathlib import Path
import pandas as pd

# Ruta base = la carpeta del proyecto (2 niveles arriba del script... [1] = 0 src, 1 "cookiecutter")
BASE_DIR = Path(__file__).resolve().parents[2]

# Carpeta de datos
DATA_DIR = BASE_DIR / "data" / "raw"

# Leer archivo
archivo = DATA_DIR / "TELECOMUNICACIONES_1.csv"
print("Ruta usada:", archivo)

ventas = pd.read_csv(archivo)
print(ventas.head())


"""EN LUGAR DE LO ANTERIOR, ES RECOMENDABLE Y MÁS SENCILLO APLICAR: cargar_datos_with_pyhere.py
   BÁSICAMENTE, PYHERE HACE LO MISMO QUE LO DE ARRIBA, PERO MÁS SENCILLO (SE PUEDE ELIMINAR ESTE ARCHIVO Y USAR SOLO EL OTRO)
"""


