import string
import re
import os
from colorama import Fore, Style, init

letter_shifts = {}
alphabet = string.ascii_uppercase

for idx, letter in enumerate(alphabet):
    shift_list = [
        alphabet[(idx + i) % 26] for i in range(-4, 5)
    ]
    letter_shifts[letter] = shift_list

def is_valid_word(word, letters):
    for idx, letter in enumerate(word):
        allowed_letters = letter_shifts[letters[idx]]
        if letter.upper() not in allowed_letters:
            return False
    return True

def process_number_sequence(number_sequence):
    steps = []
    
    adjusted_numbers = [n - 1 for n in number_sequence]
    steps.append(f"1: Subtract 1 -> {Fore.YELLOW}{adjusted_numbers}{Style.RESET_ALL}")
    
    if len(adjusted_numbers) <= 9:
        processed_numbers = [n * 3 for n in adjusted_numbers]
        steps.append(f"2: Triple(# <= 9) -> {Fore.YELLOW}{processed_numbers}{Style.RESET_ALL}")
    else:
        processed_numbers = [n * 2 for n in adjusted_numbers]
        steps.append(f"2: Double(# >= 10) -> {Fore.YELLOW}{processed_numbers}{Style.RESET_ALL}")
    
    letters = [alphabet[n % 26] for n in processed_numbers]
    steps.append(f"3: Map(A=0 to Z=25) -> {Fore.YELLOW}[{', '.join(letters)}]{Style.RESET_ALL}")
    
    return letters, steps

def get_valid_words(letters, word_size):
    valid_words = []
    try:
        with open('/usr/share/dict/words', 'r') as f:
            words = f.read().splitlines()
            total_words = len(words)
            

            matching_words = [
                word for word in words 
                if len(re.sub(r"[^a-zA-Z]", "", word)) == word_size
            ]
            total_matching = len(matching_words)

            for word in matching_words:
                word_cleaned = re.sub(r"[^a-zA-Z]", "", word)
                if is_valid_word(word_cleaned.lower(), letters):
                    valid_words.append(word)
    except FileNotFoundError:
        print("Wordlist not found.")
        total_words = 0
        total_matching = 0
    return valid_words, total_matching, total_words


def main():

    numbers_input = input("Enter the sequence of numbers (space-separated): ")
    number_sequence = [int(num) for num in numbers_input.split()]
    
    letters, steps = process_number_sequence(number_sequence)
    
    word_size = int(input("Enter the word size (e.g., 9, 10, 11): "))
    os.system('clear')
    
    valid_words, total_matching, total_words = get_valid_words(letters, word_size)
    print(f"{Fore.GREEN}┌─({Style.RESET_ALL}{Fore.BLUE}Obtaining Hat{Style.RESET_ALL}{Fore.GREEN}){Style.RESET_ALL}")
    print(f"{Fore.GREEN}│{Style.RESET_ALL}")
    # Display the results
    print(f"{Fore.GREEN}│-{Style.RESET_ALL}{Fore.BLUE}>{Style.RESET_ALL}Total words in dictionary: {Fore.YELLOW}{total_words}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}│ {Style.RESET_ALL}{Fore.YELLOW}:: {Style.RESET_ALL} Total words of size {word_size}: {Fore.YELLOW}{total_matching}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}│{Style.RESET_ALL}")
    print(f"{Fore.GREEN}│-{Style.RESET_ALL}{Fore.BLUE}>{Style.RESET_ALL}Conversion steps:")
    for step in steps:
        print(f"{Fore.GREEN}│ {Style.RESET_ALL}{Fore.YELLOW}:: {Style.RESET_ALL} {step}")
    print(f"{Fore.GREEN}│{Style.RESET_ALL}")
    print(f"{Fore.GREEN}│-{Style.RESET_ALL}{Fore.BLUE}>{Style.RESET_ALL}using sequence: {Fore.YELLOW}{', '.join(letters)}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}│ {Style.RESET_ALL}{Fore.YELLOW}:: {Style.RESET_ALL} Shifting each up or down by 4")
    print(f"{Fore.GREEN}│{Style.RESET_ALL}")
    print(f"{Fore.GREEN}│-{Style.RESET_ALL}{Fore.BLUE}>{Style.RESET_ALL}Found {len(valid_words)} out of {total_matching} {word_size}-letter words:")
    for word in valid_words:
        print(f"{Fore.GREEN}│ {Style.RESET_ALL}{Fore.YELLOW}:: {Style.RESET_ALL} {word}")
    print(f"{Fore.GREEN}│{Style.RESET_ALL}")
    print(f"{Fore.GREEN}└──({Style.RESET_ALL}{Fore.BLUE}End of List{Style.RESET_ALL}{Fore.GREEN}){Style.RESET_ALL}")
if __name__ == "__main__":
    main()
