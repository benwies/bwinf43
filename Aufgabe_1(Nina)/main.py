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
            return False, pos1  
    return True, "Gültiger Hopsitext"

def remove_invalid_word(words, invalid_index):
    del words[invalid_index]

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
        if not is_valid:
            words = current_text.split()
            invalid_pos = message
            word_index = 0
            char_count = 0
            for i, word in enumerate(words):
                word_length = len(word)
                if char_count + word_length >= invalid_pos:
                    word_index = i
                    break
                char_count += word_length + 1
            remove_invalid_word(words, word_index)
            text = words
            print(f"Das ungültige Wort an Position {invalid_pos} wurde entfernt.")
            print("Fügen Sie ein neues Wort hinzu:")
    final_text = " ".join(text)
    print("\nFinaler Text:")
    print(final_text)
    is_valid, message = check_hopsitext(final_text)
    print("Gültiger Hopsitext" if is_valid else "Kein gültiger Hopsitext")
    print(message)

if __name__ == "__main__":
    main()
