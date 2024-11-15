def calculate_jump(char):
    # Überprüft, ob das Zeichen ein normaler Buchstabe (a-z) ist
    if char.lower() in 'abcdefghijklmnopqrstuvwxyz':
        # Berechnet den Sprungwert als Position im Alphabet (a=1, b=2, ..., z=26)
        return ord(char.lower()) - ord('a') + 1
    # Überprüft, ob das Zeichen ein deutsches Sonderzeichen (ä, ö, ü, ß) ist
    elif char.lower() in 'äöüß':
        # Gibt spezielle Werte für deutsche Umlaute und das scharfe S zurück
        return {'ä': 27, 'ö': 28, 'ü': 29, 'ß': 30}[char.lower()]
    # Wenn das Zeichen kein gültiger Buchstabe oder Sonderzeichen ist, gibt 0 zurück
    return 0

def check_hopsitext(text):
    pos1, pos2 = 0, 1  # Startpositionen der beiden Springer (pos1 und pos2)
    len_text = len(text)  # Länge des Textes
    
    while pos1 < len_text and pos2 < len_text:  # Solange beide Springer im Text bleiben
        # Überspringt ungültige Zeichen, die keinen Sprungwert haben (z. B. Leerzeichen)
        while pos1 < len_text and calculate_jump(text[pos1]) == 0:
            pos1 += 1
        while pos2 < len_text and calculate_jump(text[pos2]) == 0:
            pos2 += 1
        
        # Wenn eine der Positionen das Ende des Textes erreicht, wird die Schleife beendet
        if pos1 >= len_text or pos2 >= len_text:
            break
        
        # Beide Springer bewegen sich basierend auf ihren Sprungwerten
        pos1 += calculate_jump(text[pos1])
        pos2 += calculate_jump(text[pos2])
        
        # Überprüft, ob die beiden Springer auf der gleichen Position landen (Kollision)
        if pos1 == pos2:
            return False, f"Kollision bei Position {pos1}"  # Kollision gefunden
    
    # Wenn keine Kollision gefunden wird, ist der Text gültig
    return True, "Gültiger Hopsitext"

def main():
    print("Willkommen zum Hopsitext-Generator!")
    print("Geben Sie Ihren Text ein. Drücken Sie Enter für neue Zeilen.")
    print("Geben Sie eine leere Zeile ein, um die Eingabe zu beenden.")
    
    text = []  # Liste zur Speicherung des Textes
    while True:
        input_text = input("Eingabe: ").strip()  # Eingabe des Textes durch den Benutzer
        if input_text == "":  # Wenn eine leere Zeile eingegeben wird, stoppt das Programm
            break
        
        text.append(input_text)  # Fügt den Text der Liste hinzu
        current_text = " ".join(text)  # Verbindet alle Textteile zu einer einzigen Zeichenkette
        
        # Überprüft den aktuellen Text auf Kollisionen
        is_valid, message = check_hopsitext(current_text)
        
        # Zeigt den aktuellen Text und den Status (gültig oder ungültig) an
        print("\nAktueller Text:")
        print(current_text)
        print("\nStatus:", "Gültiger Hopsitext" if is_valid else "Kein gültiger Hopsitext")
        print(message)
        print("-" * 40)  # Trennt die Ausgaben visuell

    final_text = " ".join(text)  # Finaler Text, der durch alle Eingaben des Benutzers entstanden ist
    print("\nFinaler Text:")
    print(final_text)
    
    # Endgültige Überprüfung des gesamten Textes auf Kollisionen
    is_valid, message = check_hopsitext(final_text)
    print("Gültiger Hopsitext" if is_valid else "Kein gültiger Hopsitext")
    print(message)

if __name__ == "__main__":
    main()  # Führt die main-Funktion aus, wenn das Programm gestartet wird
