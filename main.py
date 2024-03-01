# Dokumentation Repository 
# Python Version 3.10
 
# Import der Bibliotheken

# Klassenstruktur
class HelloWorld:
    def __init__(self, name):   # Konstruktor Methode welche automatisch "init"ialisiert wird.
        self.name = name

    def hello(self):
        print ("Hello World from " + self.name)  

def main():
    Josef = HelloWorld("Karl")   # Objekt Erstellung "Name"
    Josef.hello()                # Methode 

if __name__ == "__main__":      # Can get called as a script but dif. from a module 
    main()      