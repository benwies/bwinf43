def calculate_jump(char):
    if char.lower() in 'abcdefghijklmnopqrstuvwxyz':
        return ord(char.lower()) - ord('a') + 1
    elif char.lower() in 'äöüß':
        return {'ä': 27, 'ö': 28, 'ü': 29, 'ß': 30}[char.lower()]
    return 0

def check_hopsitext(text):
    pos1, pos2 = 0, 1
    len_text = len(text)
    
    while pos1 < len_text and pos2 < len_text:
        while pos1 < len_text and calculate_jump(text[pos1]) == 0:
            pos1 += 1
        while pos2 < len_text and calculate_jump(text[pos2]) == 0:
            pos2 += 1
        
        if pos1 >= len_text or pos2 >= len_text:
            break
        
        pos1 += calculate_jump(text[pos1])
        pos2 += calculate_jump(text[pos2])
        
        if pos1 == pos2:
            return False, f"Kollision bei Position {pos1}"
    
    return True, "Gültiger Hopsitext"

def main():
    print("Willkommen zum Hopsitext-Generator!")
    print("Geben Sie Ihren Text ein. Drücken Sie Enter für neue Zeilen.")
    print("Geben Sie eine leere Zeile ein, um die Eingabe zu beenden.")
    
    text = []
    while True:
        input_text = input("Eingabe: ").strip()
        if input_text == "":
            break
        
        text.append(input_text)
        current_text = " ".join(text)
        
        is_valid, message = check_hopsitext(current_text)
        
        print("\nAktueller Text:")
        print(current_text)
        print("\nStatus:", "Gültiger Hopsitext" if is_valid else "Kein gültiger Hopsitext")
        print(message)
        print("-" * 40)

    final_text = " ".join(text)
    print("\nFinaler Text:")
    print(final_text)
    print("\nEndgültiger Status:")
    is_valid, message = check_hopsitext(final_text)
    print("Gültiger Hopsitext" if is_valid else "Kein gültiger Hopsitext")
    print(message)

if __name__ == "__main__":
    main()