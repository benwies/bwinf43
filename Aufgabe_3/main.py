from itertools import combinations

def parse_data(filename):
    ranges = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        n = int(lines[0].strip())
        for line in lines[1:]:
            line = line.strip()
            if line and not line.startswith('#'):
                min_range, max_range = map(int, line.split())
                ranges.append((min_range, max_range))
    return n, ranges

def count_satisfied_members(strecken, ranges):
    satisfied_members = set()
    for i, (min_range, max_range) in enumerate(ranges):
        if any(min_length <= max_range and max_length >= min_range for min_length, max_length in strecken):
            satisfied_members.add(i + 1)
    return len(satisfied_members), satisfied_members

def find_best_routes(ranges):
    best_count = 0
    best_combinations = []
    all_possible_lengths = {length for r in ranges for length in range(r[0], r[1] + 1)}
    
    for comb in combinations(all_possible_lengths, 3):
        strecken = [(comb[0], comb[0]), (comb[1], comb[1]), (comb[2], comb[2])]
        count, satisfied_members = count_satisfied_members(strecken, ranges)
        if count > best_count:
            best_count = count
            best_combinations = [(comb, satisfied_members)]
        elif count == best_count:
            best_combinations.append((comb, satisfied_members))
    
    return best_count, best_combinations

filename = 'wandern4.txt'

n, ranges = parse_data(filename)

best_count, best_combinations = find_best_routes(ranges)

print(f"Maximale Anzahl der Teilnehmer: {best_count}")
print("Beste Kombinationen von drei Streckenlängen:")
for comb, satisfied_members in best_combinations:
    print(f"Streckenlängen: {comb}")
    print(f"Teilnehmende Mitglieder: {', '.join(map(str, satisfied_members))}")

if best_combinations:
    best_combination = best_combinations[0]
    best_lengths, best_members = best_combination
    print("\nBeste 3er-Kombination:")
    print(f"Streckenlängen: {best_lengths}")
    print(f"Teilnehmende Mitglieder: {', '.join(map(str, best_members))}")
