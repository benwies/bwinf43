personen = [
    (12, 30),  
    (23, 45),  
    (12, 40)  
    ]

def teilnehmer_zahlen(strecke, personen):
    return [i for i, (min_strecke, max_strecke) in enumerate(personen) if min_strecke <= strecke <= max_strecke]

def greedy_algorithm(personen):
    gewaehlte_strecken = []
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
        gewaehlte_strecken.append(beste_strecke)
        abgedeckte_personen.update(beste_abdeckung)
        strecken_kandidaten.discard(beste_strecke) 
    
    return gewaehlte_strecken, abgedeckte_personen

strecken, teilnehmer = greedy_algorithm(personen)

print("Gewählte Streckenlängen:", strecken)
print("Teilnehmende Personen:", list(teilnehmer))

for strecke in strecken:
    min_strecke = strecke
    max_strecke = strecke
    teilnehmer_bei_strecke = teilnehmer_zahlen(strecke, personen)
    print(f"Strecke {strecke}: Min: {min_strecke}, Max: {max_strecke}, Teilnehmende Personen: {teilnehmer_bei_strecke}")
