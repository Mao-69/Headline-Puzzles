from colorama import Fore, Style, init
import os

def create_mapping(*plain_texts):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rows = []

    for i in range(0, len(plain_texts), 2):
        plain = ''.join(filter(str.isalpha, plain_texts[i].upper()))
        cipher = ''.join(filter(str.isalpha, plain_texts[i+1].upper()))

        if len(plain) != len(cipher):
            print("Error: Plain text and cipher text must have the same length.")
            return

        rows.append([" " for _ in range(len(alphabet))])

    for j in range(0, len(plain_texts), 2):
        plain = ''.join(filter(str.isalpha, plain_texts[j].upper()))
        cipher = ''.join(filter(str.isalpha, plain_texts[j+1].upper()))
        
        for i in range(len(plain)):
            p_char = plain[i]
            c_char = cipher[i]
            
            if p_char in alphabet:
                p_index = alphabet.index(p_char)
                rows[j // 2][p_index] = c_char

    print(f"{Fore.GREEN}│-{Style.RESET_ALL}{Fore.BLUE}>{Style.RESET_ALL}  P   {alphabet}")
    print(f"{Fore.GREEN}│{Style.RESET_ALL}-------------------------------")
    for i, row in enumerate(rows):
        print(f"{Fore.GREEN}│-{Style.RESET_ALL}{Fore.BLUE}>{Style.RESET_ALL} C{i + 1}   {''.join(row)}")
    print(f"{Fore.GREEN}│{Style.RESET_ALL}")
    print(f"{Fore.GREEN}└──({Style.RESET_ALL}{Fore.BLUE}Mapped 5 of 5 ciphers{Style.RESET_ALL}{Fore.GREEN}){Style.RESET_ALL}")
    
    new_alphabet = input("Enter a 26-character sequence to remap: ").upper()

    new_rows = []

    for row in rows:
        new_row = [" " for _ in range(26)]
        used_letters = set()

        for idx, new_p in enumerate(new_alphabet):
            original_index = alphabet.index(new_p)
            original_cipher = row[original_index]

            if original_cipher != " " and original_cipher not in used_letters:
                new_row[idx] = original_cipher
                used_letters.add(original_cipher)

        new_rows.append(new_row)

    def fill_missing_letters(new_row, cipher_row, new_alphabet):
        filled_row = new_row[:]
        
        missing_letters = [i for i, char in enumerate(filled_row) if char == " "]
        
        current_index = 0
        for missing_idx in missing_letters:
            if missing_idx > 0 and filled_row[missing_idx - 1] != " ":
                prev_letter = filled_row[missing_idx - 1]
                prev_letter_index = new_alphabet.index(prev_letter)
                next_letter = new_alphabet[(prev_letter_index + 1) % 26]
                filled_row[missing_idx] = next_letter
        return filled_row

    final_new_rows = []
    for i, new_row in enumerate(new_rows):
        cipher_row = rows[i]
        new_row = fill_missing_letters(new_row, cipher_row, new_alphabet)
        final_new_rows.append(new_row)

    print(f"\n{Fore.GREEN}┌─({Style.RESET_ALL}{Fore.BLUE}Remapped Ciphers to new alphabet{Style.RESET_ALL}{Fore.GREEN}){Style.RESET_ALL}")
    print(f"{Fore.GREEN}│{Style.RESET_ALL}")
    print(f"{Fore.GREEN}│-{Style.RESET_ALL}{Fore.BLUE}>{Style.RESET_ALL}  P   {new_alphabet}")
    print(f"{Fore.GREEN}│{Style.RESET_ALL}-------------------------------")
    for i, row in enumerate(final_new_rows):
        print(f"{Fore.GREEN}│-{Style.RESET_ALL}{Fore.BLUE}>{Style.RESET_ALL} C{i + 1}   {''.join(row)}")
    print(f"{Fore.GREEN}│{Style.RESET_ALL}")
    print(f"{Fore.GREEN}└──({Style.RESET_ALL}{Fore.BLUE}Mapped 5 of 5 ciphers{Style.RESET_ALL}{Fore.GREEN}){Style.RESET_ALL}")

    wordlist_path = "/usr/share/dict/words"
    with open(wordlist_path, "r") as file:
        words = set(word.strip().upper() for word in file.readlines() if len(word.strip()) == 5)

    def search_for_words_in_columns(new_rows, alphabet):
        for col_idx in range(len(alphabet)):
            column = ''.join([row[col_idx] for row in new_rows])
            for i in range(len(column) - 5 + 1):
                word_candidate = column[i:i+5]
                if word_candidate in words:
                    print(f"{Fore.GREEN}│{Style.RESET_ALL}{Fore.YELLOW}Found word{Style.RESET_ALL} '{Fore.RED}{word_candidate}{Style.RESET_ALL}'{Fore.YELLOW} in column under letter {Style.RESET_ALL}'{Fore.RED}{alphabet[col_idx]}{Style.RESET_ALL}'")

    search_for_words_in_columns(final_new_rows, new_alphabet)

def main():
    print("Enter plain text and cipher text pairs:")
    p_1 = input("plain 1: ")
    c_1 = input("cipher  1: ")
    p_2 = input("plain 2: ")
    c_2 = input("cipher  2: ")
    p_3 = input("plain 3: ")
    c_3 = input("cipher  3: ")
    p_4 = input("plain 4: ")
    c_4 = input("cipher  4: ")
    p_5 = input("plain 5: ")
    c_5 = input("cipher  5: ")
    os.system('clear')
    print(f"{Fore.GREEN}┌─({Style.RESET_ALL}{Fore.BLUE}Mapping Ciphers to plain A-Z{Style.RESET_ALL}{Fore.GREEN}){Style.RESET_ALL}")
    print(f"{Fore.GREEN}│{Style.RESET_ALL}")
    create_mapping(p_1, c_1, p_2, c_2, p_3, c_3, p_4, c_4, p_5, c_5)


if __name__ == "__main__":
    main()
