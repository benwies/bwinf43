import os

ascii_art = """
██╗    ██╗ █████╗ ███╗   ██╗██████╗ ███████╗██████╗ ████████╗ █████╗  ██████╗ 
██║    ██║██╔══██╗████╗  ██║██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔════╝ 
██║ █╗ ██║███████║██╔██╗ ██║██║  ██║█████╗  ██████╔╝   ██║   ███████║██║  ███╗
██║███╗██║██╔══██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗   ██║   ██╔══██║██║   ██║
╚███╔███╔╝██║  ██║██║ ╚████║██████╔╝███████╗██║  ██║   ██║   ██║  ██║╚██████╔╝
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝                                                                  
"""

def menü_anzeigen():
    os.system('clear' if os.name == 'posix' else 'cls') 
    print(ascii_art)
    print("Bitte wählen Sie eine Option:")
    print("1. Datei scannen und auswählen")
    print("2. Beenden")

def option_1():
    dateien = [f for f in os.listdir('.') if f.endswith('.txt')]
    if not dateien:
        print("Keine Textdateien im Verzeichnis gefunden.")
        input("\nDrücken Sie Enter, um zum Hauptmenü zurückzukehren...")
        return

    print("Verfügbare Textdateien:")
    for idx, datei in enumerate(dateien, 1):
        print(f"{idx}. {datei}")

    try:
        auswahl = int(input("\nGeben Sie die Nummer der Datei ein, die verarbeitet werden soll: "))
        if 1 <= auswahl <= len(dateien):
            dateipfad = dateien[auswahl - 1]
            with open(dateipfad, 'r') as datei:
                zeilen = datei.readlines()
                eintragsanzahl = int(zeilen[0].strip())
                personen = [tuple(map(int, zeile.strip().split())) for zeile in zeilen[1:eintragsanzahl + 1]]
            
            print("\nVerarbeite Datei:", dateipfad)
            strecken, teilnehmer = greedy_algorithm(personen)
            
            print("Gewählte Streckenlängen:", strecken)
            print("Teilnehmende Personen:", list(teilnehmer))

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

def option_2():
    print("Programm wird beendet. Auf Wiedersehen!")

def teilnehmer_zahlen(strecke, personen):
    return [i for i, (min_strecke, max_strecke) in enumerate(personen) if min_strecke <= strecke <= max_strecke]

def greedy_algorithm(personen):
    gewählte_strecken = []
    abgedeckte_personen = set()

    strecken_kandidaten = set()
    for min_strecke, max_strecke in personen:
        strecken_kandidaten.add(min_strecke)
        strecken_kandidaten.add(max_strecke)

    for _ in range(3):
        beste_strecke = None
        beste_abdeckung = set()      

        for strecke in strecken_kandidaten:
            aktuelle_abdeckung = set(teilnehmer_zahlen(strecke, personen))
            neue_abdeckung = aktuelle_abdeckung - abgedeckte_personen 
            
            if len(neue_abdeckung) > len(beste_abdeckung):
                beste_strecke = strecke
                beste_abdeckung = neue_abdeckung
        
        if beste_strecke is None:
            beste_strecke = strecken_kandidaten.pop()
            beste_abdeckung = set(teilnehmer_zahlen(beste_strecke, personen))
        gewählte_strecken.append(beste_strecke)
        abgedeckte_personen.update(beste_abdeckung)
        strecken_kandidaten.discard(beste_strecke) 
    
    return gewählte_strecken, abgedeckte_personen

def main():
    while True:
        menü_anzeigen()
        try:
            auswahl = int(input("\nGeben Sie Ihre Wahl ein (1-2): "))
            if auswahl == 1:
                option_1()
            elif auswahl == 2:
                option_2()
                break
            else:
                print("Ungültige Auswahl. Bitte geben Sie 1 oder 2 ein.")
                input("\nDrücken Sie Enter, um zum Hauptmenü zurückzukehren...")
        except ValueError:
            print("Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
            input("\nDrücken Sie Enter, um zum Hauptmenü zurückzukehren...")

if __name__ == "__main__":
    main()
