import sys
import os
import subprocess

# Öffnet das Skript in einem neuen Terminalfenster (nur für Windows)
def open_in_new_terminal():
    if os.name == 'nt':  # Prüft, ob das OS Windows ist
        script_path = os.path.abspath(__file__)  # Absoluter Pfad des Skripts
        script_dir = os.path.dirname(script_path)  # Verzeichnis des Skripts
        # Öffnet das Skript in einem neuen cmd-Fenster
        subprocess.run(['start', 'cmd', '/k', f'cd /D {script_dir} && python {script_path}'], shell=True)
        sys.exit()  # Beendet das aktuelle Skript.

if __name__ == "__main__":
    # Falls Windows und kein interaktives Terminal, öffne das Skript neu
    if os.name == 'nt' and not sys.stdin.isatty():
        open_in_new_terminal()

# ASCII-Art für das Menü
ascii_art = """
██╗    ██╗ █████╗ ███╗   ██╗██████╗ ███████╗██████╗ ████████╗ █████╗  ██████╗ 
██║    ██║██╔══██╗████╗  ██║██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔════╝ 
██║ █╗ ██║███████║██╔██╗ ██║██║  ██║█████╗  ██████╔╝   ██║   ███████║██║  ███╗
██║███╗██║██╔══██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗   ██║   ██╔══██║██║   ██║
╚███╔███╔╝██║  ██║██║ ╚████║██████╔╝███████╗██║  ██║   ██║   ██║  ██║╚██████╔╝
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝                                                                  
"""

# Menü anzeigen und Benutzeroptionen
def menü_anzeigen():
    os.system('cls' if os.name == 'nt' else 'clear')  # Bildschirm leeren (Windows: 'cls', andere: 'clear')
    print(ascii_art)  # ASCII-Art ausgeben.
    print("Bitte wählen Sie eine Option:")  # Menütext
    print("1. Datei scannen und auswählen")  # Option 1
    print("2. Beenden")  # Option 2

# Option 1: Textdateien im aktuellen Verzeichnis scannen und verarbeiten
def option_1():
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Verzeichnis des Skripts
    
    # Alle .txt-Dateien im Verzeichnis suchen
    dateien = [f for f in os.listdir(script_dir) if f.endswith('.txt')]
    
    if not dateien:  # Wenn keine Textdateien gefunden wurden
        print("Keine Textdateien im Verzeichnis gefunden.")
        input("\nDrücken Sie Enter, um zum Hauptmenü zurückzukehren...")
        return

    # Gefundene Textdateien anzeigen
    print("Verfügbare Textdateien:")
    for idx, datei in enumerate(dateien, 1):
        print(f"{idx}. {datei}")

    try:
        # Benutzer wählt eine Datei aus
        auswahl = int(input("\nGeben Sie die Nummer der Datei ein, die verarbeitet werden soll: "))
        if 1 <= auswahl <= len(dateien):
            # Pfad zur gewählten Datei erstellen
            dateipfad = os.path.join(script_dir, dateien[auswahl - 1])
            with open(dateipfad, 'r') as datei:
                zeilen = datei.readlines()
                # Erste Zeile enthält die Anzahl der Personen
                eintragsanzahl = int(zeilen[0].strip())
                # Verarbeite die folgenden Zeilen mit den Min- und Max-Strecken
                personen = [tuple(map(int, zeile.strip().split())) for zeile in zeilen[1:eintragsanzahl + 1]]

            print("\nVerarbeite Datei:", dateipfad)
            strecken, teilnehmer = greedy_algorithm(personen)  # Greedy-Algorithmus zur Auswahl der Strecken

            # Ergebnisse anzeigen
            print("Gewählte Streckenlängen:", strecken)
            print("Teilnehmende Personen:", list(teilnehmer))

            # Zeigt für jede Strecke die Min- und Max-Werte sowie die zugeordneten Teilnehmer an
            for strecke in strecken:
                min_strecke = strecke
                max_strecke = strecke
                teilnehmer_bei_strecke = teilnehmer_zahlen(strecke, personen)
                print(f"Strecke {strecke}: Min: {min_strecke}, Max: {max_strecke}, Teilnehmende Personen: {teilnehmer_bei_strecke}")

        else:
            print("Ungültige Auswahl.")
    except ValueError:
        print("Ungültige Eingabe.")

    input("\nDrücken Sie Enter, um zum Hauptmenü zurückzukehren...")

# Option 2: Programm beenden
def option_2():
    print("Programm wird beendet. Auf Wiedersehen!")

# Bestimmt, welche Personen eine Strecke absolvieren können
def teilnehmer_zahlen(strecke, personen):
    return [i for i, (min_strecke, max_strecke) in enumerate(personen) if min_strecke <= strecke <= max_strecke]

# Greedy-Algorithmus: Wählt die besten Strecken basierend auf der Abdeckung der Teilnehmer
def greedy_algorithm(personen):
    gewählte_strecken = []  # Liste der gewählten Strecken
    abgedeckte_personen = set()  # Set der bereits abgedeckten Teilnehmer

    strecken_kandidaten = set()  # Set der möglichen Strecken
    for min_strecke, max_strecke in personen:
        strecken_kandidaten.add(min_strecke)  # Min-Strecke als Kandidat
        strecken_kandidaten.add(max_strecke)  # Max-Strecke als Kandidat

    # Wähle maximal 3 Strecken
    for _ in range(3):
        beste_strecke = None
        beste_abdeckung = set()

        # Suche die Strecke, die die meisten neuen Personen abdeckt
        for strecke in strecken_kandidaten:
            aktuelle_abdeckung = set(teilnehmer_zahlen(strecke, personen))
            neue_abdeckung = aktuelle_abdeckung - abgedeckte_personen

            if len(neue_abdeckung) > len(beste_abdeckung):
                beste_strecke = strecke
                beste_abdeckung = neue_abdeckung

        if beste_strecke is None:
            # Wenn keine Strecke optimal ist, wähle eine beliebige
            beste_strecke = strecken_kandidaten.pop()
            beste_abdeckung = set(teilnehmer_zahlen(beste_strecke, personen))
        
        gewählte_strecken.append(beste_strecke)  # Füge die beste Strecke hinzu
        abgedeckte_personen.update(beste_abdeckung)  # Aktualisiere die abgedeckten Personen
        strecken_kandidaten.discard(beste_strecke)  # Entferne die gewählte Strecke von den Kandidaten

    return gewählte_strecken, abgedeckte_personen  # Rückgabe der gewählten Strecken und abgedeckten Personen

# Hauptmenüschleife
def main():
    while True:
        menü_anzeigen()  # Zeigt das Menü an
        try:
            auswahl = int(input("\nGeben Sie Ihre Wahl ein (1-2): "))  # Nimmt Benutzerauswahl entgegen
            if auswahl == 1:
                option_1()  # Option 1 ausführen
            elif auswahl == 2:
                option_2()  # Programm beenden
                break
            else:
                print("Ungültige Auswahl. Bitte geben Sie 1 oder 2 ein.")
                input("\nDrücken Sie Enter, um zum Hauptmenü zurückzukehren...")
        except ValueError:
            print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
            input("\nDrücken Sie Enter, um zum Hauptmenü zurückzukehren...")

if __name__ == "__main__":
    main()  # Starte das Hauptmenü
