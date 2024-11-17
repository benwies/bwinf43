# Datei öffnen und Zeile für Zeile lesen
file_name = 'Idee.txt'

try:
    with open(file_name, 'r') as file:
        # Jede Zeile einzeln ausgeben
        for line in file:
            print(line.strip())  # .strip() entfernt das Zeilenumbruchzeichen
except FileNotFoundError:
    print(f"Die Datei {file_name} wurde nicht gefunden.")
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")
