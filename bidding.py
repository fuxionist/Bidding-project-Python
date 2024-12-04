import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
symbol_value ={
    "A": 6,
    "B": 2,
    "C": 3,
    "D": 4
}

def check_winnings(columns, lines, bet, symbol_value):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += bet * symbol_value[symbol]
            winning_lines.append(line+1)
    return winnings, winning_lines

def get_slot_machine_spin(ROWS, COLS, symbol_count):
    all_symbols = []
    for symbol, count in symbol_count.items():
        for _ in range(count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(COLS):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(ROWS):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end=" ")
        print()  # Move to the next row

def deposit():
    while True:
        amount = input("What is your deposit amount? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid number.")
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines.")
        else:
            print("Please enter a valid number.")
    return lines

def ask_game_rules():
    while True:
        gamerules = input("Have you read the game rules? (yes/no): ").strip().lower()
        if gamerules == "yes":
            print("Great! Let's start the game.")
            break
        elif gamerules == "no":
            print("Please make sure to read the game rules before starting.")
            break
        else:
            print("Please answer with 'yes' or 'no'.")
    return gamerules

def get_bet():
    while True:
        amount = input(f"What would you like to bet on each line? (${MIN_BET}-${MAX_BET}): ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a valid number.")
    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    ask_game_rules()

    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You don't have enough to bet. Your current balance is: ${balance}")
        else:
            print(f"You are betting ${bet} on {lines} lines. Total bet is: ${total_bet}")
            balance -= total_bet
            print(f"Remaining balance: ${balance}")
            break

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print("Slot Machine Result:")
    print_slot_machine(slots)
    winnings = check_winnings(slots, bet, lines, symbol_value)
    winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"you won ${winnings}")
    print(f"you won on lines:", *winning_lines)
    print(f"Your updated balance is: ${balance}")


if __name__ == "__main__":
    main()
