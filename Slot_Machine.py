import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

#Colunas e linhas da slot machine
ROWS = 3
COLS = 3

#Quantidade e contagem de símbolos de slot
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}
#Função pra checar se o usuário ganhou e quanto:
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns [0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
            else:
                winnings += values[symbol] * bet
                winning_lines.append(line + 1)

    return winnings, winning_lines

#Função das possibilidades de resultado do slot
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

#Função de printar os resultados da slot
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()



#Função de depósito
def deposit():
    while True:
        amount = input("Valor do depósito: R$")
        if amount.isdigit():
            amount = int(amount)
            if amount >0:
                break
            else:
                print("O depósito deve ser maior que R$0.00")
        else:
            print("Por favor, insira um número: ")
    return amount

#Função de início
def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Você não tem fundo suficiente, o seu saldo atual é de R${balance}!")
        else:
            break
    print(f"Você está apostando R${bet} em {lines} linhas. A aposta total é de:  R${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)

    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"Você ganhou R${winnings}!")
    print(f"Você ganhou na linha:", *winning_lines)

#Função de número de linhas
def get_number_of_lines():
    while True:
        lines = input("Em quantas linhas você quer apostar? (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Insira um número válido de linhas (1 a 3)")
        else:
            print("Por favor, insira um número: ")
    return lines

#Função para inserir aposta
def get_bet():
    while True:
        amount = input("Valor da aposta: R$")
        if amount.isdigit():
            amount = int(amount)
        if MIN_BET <= amount <= MAX_BET:
            break
        else:
            print(f"A aposta deve estar entre R${MIN_BET} e R${MAX_BET}")
    else:
        print("Por favor, insira um número: ")

    return amount

main()