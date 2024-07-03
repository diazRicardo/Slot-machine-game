MAX_NUMBER_LINES = 3 # max number of slot lines to bet on
MIN_BET = 1          # min bet amount to place on each line
MAX_BET = 10000      # max bet amount to place on each line


# user enters $ deposit
def deposit():
    while True:
        amount = input('Enter amount to deposit: $' )
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            print('Amount must be greater than zero.')
        else:
            print('Invalid: Enter a number.')
    return amount

# user enters number of slot lines to bet on
def number_on_lines():
    while True:
        lines = input('Enter amount to lines to bet on: ' )
        if lines.isdigit():
            lines = int(lines)
            if 0 < lines <= MAX_NUMBER_LINES:
                break
            print('Invalid: Amount must be between 1 and 3.')
        else:
            print('Invalid: Enter a number.')
    return lines

# user enters how much $ to bet on each line
def bet():
    while True:
        bet_amount = input('Enter amount to bet on each line: $' )
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if MIN_BET <= bet_amount <= MAX_BET: 
                break
            print(f'Invalid: Amount must be between ${MIN_BET} - ${MAX_BET}.')
        else:
            print('Invalid: Enter a number.')
    return bet_amount

def main():
    balance = deposit() # add deposit to user balance
    lines = number_on_lines()

    while True:
        bet_amount = bet()
        total_bet = bet_amount * lines
        if total_bet > balance:
            print(f"Not enough funds in balance. Balance: ${balance}")
        else:
            break
        
    print(f"Beting ${bet_amount} on {lines} line.")
    print(f"Total bet: ${total_bet}")

   
main()
