import pyhere 

# Directorio raíz del proyecto
PROJECT_DIR = pyhere.here() 
DATA_DIR = PROJECT_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
