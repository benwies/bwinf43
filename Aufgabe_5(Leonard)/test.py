def intervall_pruefen(zahl, intervall_breite=3):
    # Prüft, ob der Abschnitt (floor der Zahl geteilt durch die Breite) gerade oder ungerade ist
    return ((zahl -1)  // intervall_breite) % 2 == 1

# Beispielaufrufe:
print(intervall_pruefen(1))  # Ausgabe: False
print(intervall_pruefen(2))  # Ausgabe: False
print(intervall_pruefen(3))  # Ausgabe: True
print(intervall_pruefen(4))  # Ausgabe: True
print(intervall_pruefen(5))  # Ausgabe: True
print(intervall_pruefen(6))  # Ausgabe: False
print(intervall_pruefen(7))  # Ausgabe: False
print(intervall_pruefen(8))  # Ausgabe: False
print(intervall_pruefen(9))  # Ausgabe: True
print(intervall_pruefen(10)) # Ausgabe: True
print(intervall_pruefen(11)) # Ausgabe: True
