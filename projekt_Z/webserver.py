import http.server
import socketserver
import os

# Definieren des Verzeichnisses mit den HTML-Dateien
document_root = "/data/html"

# Erstellen eines HTTP-Servers
class Webserver(http.server.SimpleHTTPRequestHandler):
    # Überschreiben der Methode, um den Pfad zu den HTML-Dateien anzupassen
    def translate_path(self, path):
        # Entfernen des führenden Schrägstrichs
        path = path[1:]
        # Zurückgeben des Pfads im Dokumentenstammverzeichnis
        return os.path.join(document_root, path)

# Starten des Servers auf Port 8000
with socketserver.TCPServer(("", 8000), Webserver) as httpd:
    print("Webserver gestartet auf Port 8000")
    httpd.serve_forever()