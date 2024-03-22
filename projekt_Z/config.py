import json
import os

from projekt_Z.logger import log_error

# Pfad zur JSON-Konfigurationsdatei
CONFIG_FILE_PATH = os.path.join(os.getcwd(), 'config.json')

# Funktion zum Laden der Konfigurationsdaten aus der JSON-Datei
def load_config():
    try:
        with open(CONFIG_FILE_PATH, "r") as config_file:
            config_data = json.load(config_file)
        return config_data
    except Exception as e:
        # Fehlerbehandlung, falls die Konfigurationsdatei nicht geladen werden kann
        log_error(f"Fehler beim laden der Konfiguration config.json: {e}")
        return {}

# Laden der Konfigurationsdaten
config_data = load_config()
