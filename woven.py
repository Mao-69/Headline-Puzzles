import os
from colorama import Fore, Style, init
import sys
import subprocess

init(autoreset=True)

def display_menu():
    print()
    print(f"{Fore.GREEN}┌─({Style.RESET_ALL}{Fore.BLUE}Woven{Style.RESET_ALL}{Fore.GREEN})─[{Style.RESET_ALL}{Fore.BLUE}Version: 1.0{Style.RESET_ALL}{Fore.GREEN}]{Style.RESET_ALL}")
    print(f"{Fore.GREEN}│{Style.RESET_ALL}")
    print(f"{Fore.GREEN}│ {Style.RESET_ALL}{Style.DIM}\"Xeoms bptw feg nelz ov wpz reumzuvwemz ea ptloms tjgmxtmrz om fegu noaz\"{Style.RESET_ALL}")

def help_menu():
    print(f"{Fore.GREEN}│{Style.RESET_ALL}")
    print(f"{Fore.GREEN}│-{Style.RESET_ALL}{Fore.BLUE}>{Style.RESET_ALL} HELP - {Fore.BLUE}Show Help Menu{Style.RESET_ALL}")
    print(f"{Fore.GREEN}│-{Style.RESET_ALL}{Fore.BLUE}>{Style.RESET_ALL} SOLVE CIPHER - {Fore.BLUE}Solve cipher{Style.RESET_ALL}")
    print(f"{Fore.GREEN}│-{Style.RESET_ALL}{Fore.BLUE}>{Style.RESET_ALL} PLAIN A TO Z MAP - {Fore.BLUE}Map ciphers to plain a to z{Style.RESET_ALL}")
    print(f"{Fore.GREEN}│-{Style.RESET_ALL}{Fore.BLUE}>{Style.RESET_ALL} GEOMETRIC CHAINING - {Fore.BLUE}Generate Geometric Chains{Style.RESET_ALL}")
    print(f"{Fore.GREEN}│-{Style.RESET_ALL}{Fore.BLUE}>{Style.RESET_ALL} GET SETTING - {Fore.BLUE}Get the setting{Style.RESET_ALL}")
    print(f"{Fore.GREEN}│-{Style.RESET_ALL}{Fore.BLUE}>{Style.RESET_ALL} GET KEY - {Fore.BLUE}Obtain the Key{Style.RESET_ALL}")
    print(f"{Fore.GREEN}│-{Style.RESET_ALL}{Fore.BLUE}>{Style.RESET_ALL} GET HAT - {Fore.BLUE}Obtain the Hat{Style.RESET_ALL}")
    print(f"{Fore.GREEN}│-{Style.RESET_ALL}{Fore.BLUE}>{Style.RESET_ALL} LETTER GRID - {Fore.BLUE}Spawn a letter grid{Style.RESET_ALL}")
    print(f"{Fore.GREEN}│-{Style.RESET_ALL}{Fore.BLUE}>{Style.RESET_ALL} DECIMATE SEQUENCE - {Fore.BLUE}Decimate a 26-long sequence by 3, 5, 7, 9, 11{Style.RESET_ALL}")
    print(f"{Fore.GREEN}│{Style.RESET_ALL}")
    print(f"{Fore.GREEN}└──({Style.RESET_ALL}{Fore.BLUE}End of List{Style.RESET_ALL}{Fore.GREEN}){Style.RESET_ALL}")

def process_ciphers():
    print("Please enter 5 ciphers:")
    ciphers = []
    for i in range(1, 6):
        cipher = input(f"Enter cipher {i}: ")
        ciphers.append(cipher)
    os.system('clear')
    print(f"{Fore.GREEN}┌─({Style.RESET_ALL}{Fore.BLUE}Decoding Ciphers{Style.RESET_ALL}{Fore.GREEN}){Style.RESET_ALL}")
    print(f"{Fore.GREEN}│{Style.RESET_ALL}")
    for cipher in ciphers:
        print(f"{Fore.GREEN}│-{Style.RESET_ALL}{Fore.BLUE}>{Style.RESET_ALL} {Fore.BLUE}{cipher}{Style.RESET_ALL}")
        escaped_cipher = cipher.replace("'", "\\'")
        os.system(f"python3 modules/solve_ciphers.py \"{escaped_cipher}\"")
        print(f"{Fore.GREEN}│{Style.RESET_ALL}-------------------------------")
    print(f"{Fore.GREEN}│{Style.RESET_ALL}")
    print(f"{Fore.GREEN}└──({Style.RESET_ALL}{Fore.BLUE}Decoded 5 of 5 ciphers{Style.RESET_ALL}{Fore.GREEN}){Style.RESET_ALL}")

def main():
    while True:
        os.system('clear')
        display_menu()
        print(f"{Fore.GREEN}│{Style.RESET_ALL}")
        option = input(f"{Fore.GREEN}└──{Style.RESET_ALL}{Fore.BLUE}$ {Style.RESET_ALL}").strip().lower()

        if option == "help":
            os.system('clear')
            display_menu()
            help_menu()
            input("Press any key to continue...")
        elif option == "solve cipher":
            os.system('clear')
            display_menu()
            process_ciphers()
            input("Press any key to continue...")
        elif option == "letter grid":
            os.system('clear')
            display_menu()
            subprocess.Popen(["python3", "modules/letter_grid.py"])
            input("Press any key to continue...")
        elif option == "decimate sequence":
            os.system('clear')
            display_menu()
            os.system('python3 modules/decimate_sequence.py')
            input("Press any key to continue...")
        elif option == "plain a to z map":
            os.system('clear')
            display_menu()
            os.system('python3 modules/plain_a_z_map.py')
            input("Press any key to continue...")
        elif option == "geometric chaining":
            os.system('clear')
            print(f"{Fore.GREEN}┌─({Style.RESET_ALL}{Fore.BLUE}Geometric Chaining{Style.RESET_ALL}{Fore.GREEN}){Style.RESET_ALL}")
            os.system('python3 modules/geometric_chain.py')
            input("Press any key to continue...")
        elif option == "get setting":
            os.system('clear')
            print(f"{Fore.GREEN}┌─({Style.RESET_ALL}{Fore.BLUE}Obtain Setting{Style.RESET_ALL}{Fore.GREEN}){Style.RESET_ALL}")
            os.system('python3 modules/new_map.py')
            input("Press any key to continue...")
        elif option == "get hat":
            os.system('clear')
            os.system('python3 modules/get_hat.py')
            input("Press any key to continue...")
        elif option == "get key":
            os.system('clear')
            os.system('python3 modules/get_key.py')
            input("Press any key to continue...")
        elif option == "exit":
            os.system('clear')
            input("Press any key to exit...")
            os.system('clear')
            break
        else:
            print("Invalid option. Please try again.")
            input("Press any key to continue...")

if __name__ == "__main__":
    main()
