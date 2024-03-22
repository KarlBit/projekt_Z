import logging
import os

# Erstelle einen Ordner für die Logdateien, falls er nicht existiert
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# Konfiguration des Root-Loggers
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Fehler-Logger
error_logger = logging.getLogger("error")
error_logger.setLevel(logging.ERROR)

# Handler für Fehler-Logger, der in die Datei error.log schreibt
error_file_handler = logging.FileHandler(os.path.join(log_dir, "error.log"))
error_file_handler.setLevel(logging.ERROR)
error_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
error_file_handler.setFormatter(error_formatter)
error_logger.addHandler(error_file_handler)

# Zugriffs-Logger
zugriff_logger = logging.getLogger("zugriff")
zugriff_logger.setLevel(logging.INFO)

# Handler für Zugriffs-Logger, der in die Datei zugriff.log schreibt
zugriff_file_handler = logging.FileHandler(os.path.join(log_dir, "zugriff.log"))
zugriff_file_handler.setLevel(logging.INFO)
zugriff_formatter = logging.Formatter("%(asctime)s - %(message)s")
zugriff_file_handler.setFormatter(zugriff_formatter)
zugriff_logger.addHandler(zugriff_file_handler)

def log_error(message):
    error_logger.error(message)

def log_info(message):
    zugriff_logger.info(message)

def log_http_request(method, url, status_code):
    zugriff_logger.info(f"HTTP-Anfrage: {method} {url} - Status: {status_code}")