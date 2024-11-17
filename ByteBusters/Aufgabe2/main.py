from collections import defaultdict, deque
import os

# Funktion zum Einlesen der Datei
def read_input(file):
    with open(file, 'r') as f:
        # Erste Zeile:
        # n (Anzahl der Klausuren),
        # m (Gesamtzahl an Aufgaben),
        # k (Anzahl an Aufgaben für welche eine gute Anordnung gefunden werden soll)
        n, m, k = map(int, f.readline().split())

        # Die nächsten n Zeilen: die Klausuren
        exams = [f.readline().strip().split(" < ") for _ in range(n)]

        # Letzte Zeile: Aufgaben, welche sortiert werden sollen
        sort = f.readline().strip().split()

    return exams, sort

# Funktion zum Aufbauen des Graphen
def build_graph(exams):
    # Adjazenzliste erstellen
    graph = defaultdict(list)

    # Durch alle Klausuren iterieren
    for exam in exams:
        # Durch alle Aufgaben iterieren
        for i in range(len(exam) - 1):
            # Die Beziehungen finden
            node_from, node_to = exam[i], exam[i + 1]

            # Falls die Beziehung noch nicht existiert
            if node_to not in graph[node_from]:
                graph[node_from].append(node_to)

    # Rückgabe des Graphen
    return graph

# Funktion zum Zusammenfügen, falls sich zwei Listen überlappen
def merge_overlapping_lists(lists):
    result = []

    for current_list in lists:
        # Prüfe, ob das Element der aktuellen Liste in einer der bereits vorhandenen Listen im Ergebnis ist
        if result and any(set(current_list).intersection(r) for r in result):
            # Wenn es eine Überschneidung gibt, finde die überschneidende Liste und füge Elemente zusammen
            for r in result:
                if set(current_list).intersection(r):
                    r.extend(x for x in current_list if x not in r)
                    break
        else:
            # Wenn keine Überschneidung vorhanden ist, füge die Liste zu den Ergebnissen hinzu
            result.append(current_list[:])

    return result

# Alle Konflikte erkennen mit DFS
def find_conflicts(graph):
    visited = set()
    conflicts = []

    def dfs(node, path):
        if node in path:
            # Konflikt gefunden
            cycle_start = path.index(node)
            conflicts.append(path[cycle_start:])
            return
        if node in visited:
            return

        visited.add(node)
        path.append(node)
        for neighbor in graph.get(node, []):
            dfs(neighbor, path)
        path.pop()

    for node in graph:
        if node not in visited:
            dfs(node, [])

    return conflicts

# Fasst Konflikte in Gruppen zusammen (Gleich schwere Aufgaben)
def merge_conflicting_nodes(graph):
    conflicts = find_conflicts(graph)
    new_conflicts = merge_overlapping_lists(conflicts)

    # Jeden Konflikt gruppieren
    for conflict in new_conflicts:
        # Neuen Knoten generieren
        group_node = "/".join(conflict)
        graph[group_node] = []
        for conflict_node in conflict:
            # Alle Beziehungen zur Gruppe hinzufügen
            for neighbor in graph[conflict_node]:
                if neighbor not in graph[group_node]:
                    graph[group_node].append(neighbor)
            # Den alten Knoten löschen
            graph.pop(conflict_node)

        # Durch alle Knoten gehen
        for node in graph:
            for conflict_node in conflict:
                # Falls ein Konfliktknoten gefunden wird, wird dieser gelöscht
                if conflict_node in graph[node]:
                    graph[node].remove(conflict_node)
                    # Falls noch nicht vorhanden wird die neue Gruppe hinzugefügt
                    if group_node not in graph[node] and group_node != node:
                        graph[node].append(group_node)

    return graph, new_conflicts

# Funktion zur topologischen Sortierung nach Kahns Algorithmus
def top_sort(graph):
    # In-Degree definieren
    indegree = defaultdict(int)
    # Indegree berechnen
    for node in graph:
        for neighbor in graph[node]:
            # Inkrementiere den In-Degree des Nachfolgeknotens
            indegree[neighbor] = indegree.get(neighbor, 0) + 1

    # Alle Knoten sollen im In-Degree sein (wenn keine Vorgänger dann 0)
    indegree.update({node: indegree[node] for node in graph})

    # Alle Knoten mit dem Indegree 0 werden zur queue hinzugefügt
    queue = deque([node for node in indegree if indegree[node] == 0])

    # Alle sortierten Aufgaben (Endergebnis)
    sorted_nodes = []

    # Bis die Warteschlange am Ende ist
    while queue:
        # Der erste Knoten aus der Warteschlange wird entnommen und anschließend zu den sortierten Knoten hinzugefügt.
        node = queue.popleft()
        sorted_nodes.append(node)

        # Alle In-Degrees der benachbarten Knoten werden um 1 herabgesetzt
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            # Falls der In-Degree der Nachbarn nun 0 ist, wird dieser zu den sortierten Knoten hinzugefügt
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_nodes

# Main-Klasse
def main(file):
    # Setze das Arbeitsverzeichnis auf das Verzeichnis, in dem das Skript liegt, musste abgepasst werden wegen Problemen mit Windows
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    # Überprüfen, ob die Datei existiert
    if os.path.exists(file):
        # Datei einlesen
        exams, sort = read_input(file)
        print("Zu sortierende Aufgaben:", ", ".join(sort))

        # gerichteten Graph aufbauen
        graph = build_graph(exams)
        # Alle Konflikte zu gleich schweren Aufgaben zusammenfassen
        new_graph, conflicts = merge_conflicting_nodes(graph)
        # topologische Sortierung des Graphen
        sorted_nodes = top_sort(new_graph)

        # Ergebnisliste
        filtered_sorted_nodes = []
        # Die Knoten richtig sortieren. Von den gleich schweren wird auch nur die gefragte ausgegeben.
        for node in sorted_nodes:
            for tosort in sort:
                if "/" in node:
                    parts = node.split('/')

                    # Nur die Teile, die in der sort-Liste enthalten sind, beibehalten
                    filtered_parts = [part for part in parts if part in sort]

                    # Wenn die gewünschte Aufgabe in einem Teil der Gruppe ist
                    if filtered_parts:
                        # Den neuen Knoten in der Reihenfolge der gefragten Teile anlegen
                        new_node = '/'.join(filtered_parts)
                        if new_node not in filtered_sorted_nodes:
                            filtered_sorted_nodes.append(new_node)
                else:
                    # Für einfache Knoten
                    if tosort == node and node not in filtered_sorted_nodes:
                        filtered_sorted_nodes.append(node)


        print("Eine gute Anordnung wäre: " + " < ".join(filtered_sorted_nodes))

        # Ausgabe der gleich schweren Aufgaben
        if conflicts:
            print("Gleich schwere Aufgaben:")
            for conflict in conflicts:
                print(f"- Die Aufgaben {', '.join(conflict)} sind gleich schwierig")
        else:
            print("Keine Konflikte entdeckt.")
    else:
        print(f"Die Datei {file} wurde nicht gefunden.")

# Beispiel
if __name__ == '__main__':
    filename = 'schwierigkeiten0.txt'
    main(filename)
