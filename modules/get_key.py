import sys
import time
from colorama import Fore, Style, init
import os

def create_vertical_groups(sequence):
    sequence_list = sequence.split()
    groups = []
    for i in range(len(sequence_list) - 1, 1, -1):
        group = sequence_list[i-2:i+1]
        groups.append(group)
    return groups

def sort_by_last_letter(groups):
    return sorted(groups, key=lambda x: x[-1])

def display_matrix(groups):
    max_length = max(len(group) for group in groups)
    matrix = ['' for _ in range(max_length)]
    
    for group in groups:
        for i in range(len(group)):
            matrix[i] += group[i] + ' '
    print(f"{Fore.GREEN}┌─({Style.RESET_ALL}{Fore.BLUE}Decoding Ciphers{Style.RESET_ALL}{Fore.GREEN}){Style.RESET_ALL}")
    print(f"{Fore.GREEN}│-{Style.RESET_ALL}{Fore.BLUE}>{Style.RESET_ALL}MATRIX -")
    print(f"{Fore.GREEN}│{Style.RESET_ALL}----------------------------------------")
    for row in matrix:
        print(f"{Fore.GREEN}│ {Style.RESET_ALL}{Fore.YELLOW}:: {Style.RESET_ALL}{row.strip()}")

    return matrix
    print(f"{Fore.GREEN}│{Style.RESET_ALL}")

def load_dictionary():
    with open("/usr/share/dict/words", "r") as f:
        return set(word.strip().lower() for word in f.readlines())

def find_words_in_matrix(matrix, dictionary):
    found_words = []
    for i, row in enumerate(matrix):
        row_str = row.replace(" ", "")
        print(f"{Fore.GREEN}│{Style.RESET_ALL}")
        print(f"{Fore.GREEN}│-{Style.RESET_ALL}{Fore.BLUE}>{Style.RESET_ALL}Row {i + 1} as string: {row_str}")

        for length in range(3, len(row_str) + 1):
            for j in range(len(row_str) - length + 1):
                substring = row_str[j:j + length]
                sys.stdout.write(f"\r{Fore.GREEN}│ {Style.RESET_ALL}{Fore.YELLOW}:: {Style.RESET_ALL}Checking substring: {substring}")  
                sys.stdout.flush()

                time.sleep(0.01)

                if substring.lower() in dictionary:
                    found_words.append((i + 1, substring))
                    sys.stdout.write(f"\rWord '{substring.upper()}' found in row {i + 1}")
                    sys.stdout.flush()
                    time.sleep(0.1)

        print()

    return found_words

sequence = input('26-long sequence :: ')
os.system('clear')
groups = create_vertical_groups(sequence)
sorted_groups = sort_by_last_letter(groups)
matrix = display_matrix(sorted_groups)
dictionary = load_dictionary()
found_words = find_words_in_matrix(matrix, dictionary)

if found_words:
    print(f"{Fore.GREEN}│{Style.RESET_ALL}")
    print(f"{Fore.GREEN}│-{Style.RESET_ALL}{Fore.BLUE}>{Style.RESET_ALL}Summary of found words:")
    for row_num, word in found_words:
        print(f"{Fore.GREEN}│ {Style.RESET_ALL}{Fore.YELLOW}:: {Style.RESET_ALL}Word '{word.upper()}' found in row {row_num}")
else:
    print("No valid words found in the matrix.")
print(f"{Fore.GREEN}└──({Style.RESET_ALL}{Fore.BLUE}End of list{Style.RESET_ALL}{Fore.GREEN}){Style.RESET_ALL}")
