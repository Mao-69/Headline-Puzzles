from colorama import Fore, Style, init
import os

def process_sequence():

    input_sequence = input("26-long sequence? ")

    if len(input_sequence) != 26:
        print("Error: Input must be exactly 26 characters long.")
        return
    os.system('clear')
    steps = [3, 5, 7, 9, 11]
    results = {}

    for step in steps:
        decimated = ""
        length = len(input_sequence)
        index = 0

        while len(decimated) < 26:
            char = input_sequence[index]

            if char not in decimated:
                decimated += char

            index += step

            if index >= length:
                index -= length

        results[step] = decimated

    BLUE = f"{Fore.BLUE}"
    RESET = f"{Style.RESET_ALL}"

    print(f"{Fore.GREEN}┌─({Style.RESET_ALL}{Fore.BLUE}{input_sequence}{Style.RESET_ALL}{Fore.GREEN}){Style.RESET_ALL}")
    print(f"{Fore.GREEN}│{Style.RESET_ALL}")
    
    for step in steps:
        formatted_decimated = " ".join(
            f"{BLUE}{char}{RESET}" if char in "vwxyz" else char
            for char in results[step]
        )
        print(f"{Fore.GREEN}│-{Style.RESET_ALL}{Fore.BLUE}>{Style.RESET_ALL} {formatted_decimated} {Fore.GREEN}│{Style.RESET_ALL} {step}")
    print(f"{Fore.GREEN}│{Style.RESET_ALL}")
    print(f"{Fore.GREEN}└──({Style.RESET_ALL}{Fore.BLUE}Decimated by | 3, 5, 7, 9, 11{Style.RESET_ALL}{Fore.GREEN}){Style.RESET_ALL}")

if __name__ == "__main__":
    process_sequence()
