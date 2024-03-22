# Import der Bibilotheken

# Import eigener Module 
from projekt_Z.webserver import start_server
from projekt_Z.logger import log_error

def main():
    try:
        start_server()
    except Exception as e:
        log_error(f"Fehler beim Starten des Servers: {e}")

if __name__ == "__main__":
    main()