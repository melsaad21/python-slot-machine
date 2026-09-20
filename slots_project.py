import random  # imports the random module so that you can get random numbers and stuff


MAX_LINES = 3  # constant value and does not change, hence the all capitals
MAX_BET = 10500  # maximum amount the user can bet on each line
MIN_BET = 1  # minimum amount the user can bet

ROWS = 3  # Makes the slot machine 3 by 3, like a normal slot machine
COLS = 3


# Specify how many of each symbol are available.
# This dictionary helps control the odds of getting each symbol.
symbol_count = {
    "A": 3,
    "B": 4,
    "C": 1,
    "D": 9
}

# The payout multiplier for each symbol.
symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []

    # Loop through every line that the user chose to bet on.
    for line in range(lines):
        # Start by checking the symbol in the first column of the current row.
        symbol = columns[0][line]

        # Compare that symbol with the symbol in the same row of every column.
        for column in columns:
            symbol_to_check = column[line]

            # If one symbol does not match, this line is not a winner.
            if symbol != symbol_to_check:
                break

        # This else belongs to the for loop.
        # It only runs if the loop finishes without hitting break.
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


# Generate one spin of the slot machine.
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []  # make a list

    # .items() gives us both the symbol and how many times it should appear.
    for symbol, count in symbols.items():
        for _ in range(count):
            # _ is used because we do not actually need the loop variable.
            all_symbols.append(symbol)

    columns = []

    for _ in range(cols):
        column = []

        # [:] creates a copy so changing current_symbols
        # does not change the original all_symbols list.
        current_symbols = all_symbols[:]

        for _ in range(rows):
            # Pick a random symbol from the available symbols.
            value = random.choice(current_symbols)

            # Remove the specific symbol we picked from this column's copy.
            current_symbols.remove(value)

            column.append(value)

        columns.append(column)

    return columns


# Makes the slot machine print horizontally by rows instead of as separate columns.
def print_slot_machine(columns):
    for row in range(len(columns[0])):

        # enumerate gives both the index and the individual column.
        for i, column in enumerate(columns):

            if i != len(columns) - 1:
                print(column[row], end=" | ")

            else:
                print(column[row], end="")

        # Move to the next line after a full row has printed.
        print()


# Collect the user's starting deposit.
def deposit():
    while True:
        amount = input("How much cash would you like to deposit? $")

        # isdigit checks that the user's input contains numbers.
        if amount.isdigit():
            amount = int(amount)

            if amount > 0:
                break

            else:
                print("Cash amount must be greater than 0.")

        else:
            print("Please enter a number.")

    return amount


# Ask the user how many slot machine lines they want to bet on.
def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" +
            str(MAX_LINES) +
            ")? "
        )

        if lines.isdigit():
            lines = int(lines)

            if 1 <= lines <= MAX_LINES:
                break

            else:
                print("Please enter a valid number of lines.")

        else:
            print("Please enter a number.")

    return lines


# Ask the user how much they want to bet on each line.
def get_bet(balance):
    while True:
        bet = input(
            f"How much would you like to bet on each line? "
            f"You have ${balance} remaining: $"
        )

        if bet.isdigit():
            bet = int(bet)

            if MIN_BET <= bet <= MAX_BET:
                break

            else:
                print(
                    f"Amount must be between ${MIN_BET} and ${MAX_BET}."
                )

        else:
            print("Enter a number.")

    return bet


# Run one complete spin of the slot machine.
def spin(balance):
    lines = get_number_of_lines()

    while True:
        bet = get_bet(balance)

        # The total amount being bet is the bet per line
        # multiplied by the number of lines.
        total_bet = bet * lines

        if total_bet > balance:
            short = total_bet - balance

            print("You do not have enough cash to bet that amount!")
            print(
                f"You need ${total_bet}. "
                f"You have ${balance}. "
                f"You are ${short} short!"
            )

        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. "
        f"Your total bet is ${total_bet}."
    )

    # Generate and display the slot machine.
    slots = get_slot_machine_spin(
        ROWS,
        COLS,
        symbol_count
    )

    print_slot_machine(slots)

    # Check the result of the spin.
    winnings, winning_lines = check_winnings(
        slots,
        lines,
        bet,
        symbol_values
    )

    print(f"You won ${winnings}!")

    if winning_lines:
        print("You won on line(s):", *winning_lines)
    else:
        print("No winning lines.")

    # Subtract the bet and add the winnings.
    return winnings - total_bet


def main():
    balance = deposit()

    while True:
        print(f"\nCurrent balance is ${balance}")

        # Without money remaining, the user can no longer place a valid bet.
        if balance <= 0:
            print("You are out of cash!")
            break

        user_decision = input(
            "Press ENTER to spin! (Type EXIT to quit): "
        )

        if user_decision.lower() == "exit":
            break

        balance += spin(balance)

    print(f"You EXITED with ${balance}!")


# Only run main automatically when this file itself is executed.
if __name__ == "__main__":
    main()