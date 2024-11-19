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
