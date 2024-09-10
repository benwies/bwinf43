def einlesen_datei(dateiname):
    with open(dateiname, 'r') as file:
        n = int(file.readline().strip())
        strecken = []
        for _ in range(n):
            min_strecke, max_strecke = map(int, file.readline().strip().split())
            strecken.append((min_strecke, max_strecke))
    
    return strecken

def main():
    dateiname = 'wandern1.txt'  
    strecken = einlesen_datei(dateiname)
    
    print("Anzahl der Personen:", len(strecken))
    for min_strecke, max_strecke in strecken:
        print(f"Minimale Strecke: {min_strecke}, Maximale Strecke: {max_strecke}")

if __name__ == "__main__":
    main()
