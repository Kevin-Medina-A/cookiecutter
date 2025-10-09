import sys
import pandas as pd
from pathlib import Path

# Agrega la raíz del proyecto (donde está paths.py) al sys.path
sys.path.append(str(Path(__file__).resolve().parents[2]))

from paths import RAW_DIR
archivo = RAW_DIR / "TEL.csv"

ventas = pd.read_csv(archivo)
print(ventas.head())

