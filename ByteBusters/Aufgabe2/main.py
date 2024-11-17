from collections import defaultdict, deque

# Funktion zum einlesen der Datei
def read_input(filename):
    with open(filename, 'r') as f:
        # Erste Zeile: n, m, k
        n, m, k = map(int, f.readline().split())

        # Die Nächsten n Zeilen: die Klausuren
        exams = [f.readline().strip().split(" < ") for _ in range(n)]

        # Letzte Zeile: Aufgabe welche sortiert werden sollen
        sort = f.readline().strip().split()

    return exams, sort

# Funktion zum Aufbauen des Graphen
def build_graph(exams):
    graph = defaultdict(list)
    indegree = defaultdict(int)

    # Durch alle Klausuren iterieren und Graphen aufbauen
    for exam in exams:
        for i in range(len(exam) - 1):
            u, v = exam[i], exam[i + 1]
            if v not in graph[u]:
                graph[u].append(v)
                indegree[v] += 1
            if u not in indegree:
                indegree[u] = 0  # Falls der Knoten davor nicht im indegree steht

    return graph, indegree

# Funktion zur topologischen Sortierung nach Kahn's Algorithmus
def top_sort(tasks, graph, indegree):
    # Hinzufügen des Knoten mit dem Eingangsgrad 0 zur Queue
    queue = deque([task for task in tasks if indegree[task] == 0])
    sorted_tasks = []
    conflicts = set()

    # Algorithmus
    while queue:
        node = queue.popleft()
        sorted_tasks.append(node)

        for n in graph[node]:
            indegree[n] -= 1
            if indegree[n] == 0:
                queue.append(n)

    # Überprüfen auf Konflikte in der topologischen Sortierung
    task_positions = {task: idx for idx, task in enumerate(sorted_tasks)}

    for task in graph:
        for successor in graph[task]:
            if successor in task_positions and task_positions[task] > task_positions[successor]:
                conflicts.add((task, successor))

    remaining = [task for task in tasks if indegree[task] > 0]
    print(f"Topologische Sortierung: {sorted_tasks}")  # Debugging-Ausgabe
    print(f"Nicht sortierte Aufgaben: {remaining}")  # Debugging-Ausgabe
    return sorted_tasks, remaining, conflicts

# Main-Klasse
def main(filename):
    # Datei einlesen
    exams, sort = read_input(filename)
    print(f"Zu sortierende Aufgaben: {sort}")

    # Graph aufbauen
    graph, indegree = build_graph(exams)

    # Topologische Sortierung
    sorted_tasks, remaining, conflicts = top_sort(sort, graph, indegree)

    filtered_sorted_tasks = [task for task in sorted_tasks if task in sort]

    # Ergebnis
    if len(filtered_sorted_tasks) == len(sort):
        print("Eine gute Anordnung wäre: " + " < ".join(filtered_sorted_tasks))
    else:
        print("Teilweise Anordnung:", " < ".join(filtered_sorted_tasks))

    # Falls konflikte
    if conflicts:
        print("Konflikte entdeckt:")
        for u, v in conflicts:
            print(f"Es entsteht ein Konflikt zwischen {u} und {v}")
    else:
        print("Keine Konflikte entdeckt.")

# Beispiel
if __name__ == '__main__':
    filename = 'schwierigkeiten0.txt'
    main(filename)