import os
from colorama import Fore, Style, init

grid = []
seq1 = ""
seq2 = ""
horizontal_spacing = 2

def initialize_grid():
    global grid
    grid_size = max(len(seq1) * horizontal_spacing, len(seq2)) + 10
    grid = [[" " for _ in range(grid_size)] for _ in range(grid_size)]

def add_horizontal_sequence():
    global seq1
    seq1 = input("Enter the horizontal sequence: ").strip()
    initialize_grid()
    
    x_start = 5
    y_start = len(grid) // 2
    
    for i, letter in enumerate(seq1):
        grid[y_start][x_start + i * horizontal_spacing] = letter

    print("Horizontal sequence added successfully.")
    print_grid()

def add_vertical_sequence():
    global seq2
    seq2 = input("Enter the vertical sequence: ").strip()

    shared_letters = [(i, j) for i, letter1 in enumerate(seq1) for j, letter2 in enumerate(seq2) if letter1 == letter2]

    if not shared_letters:
        print("No shared letters found between the sequences.")
        return
    
    x_start = 5
    y_start = len(grid) // 2
    

    for i, j in shared_letters:
        vertical_x = x_start + i * horizontal_spacing

        for k, letter in enumerate(seq2):
            grid[y_start + (k - j)][vertical_x] = letter

    print(f"Vertical sequence added with {len(shared_letters)} shared letters.")
    print_grid()

def print_grid():
    os.system('clear')
    for row in grid:
        print("".join(row).rstrip())

def interactive_menu():
    while True:
        option = input(f"{Fore.GREEN}└──{Style.RESET_ALL}{Fore.BLUE}$ {Style.RESET_ALL}").strip().lower()

        if option == "add horizontal sequence":
            add_horizontal_sequence()
        elif option == "add vertical sequence":
            add_vertical_sequence()
        elif option == "exit":
            os.system('clear')
            break
        else:
            print("Invalid option. Please try again.")
            input("Press any key to continue...")

interactive_menu()
