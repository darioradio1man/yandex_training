def deposit(name, the_sum):
    bank[name] = bank.get(name, 0) + int(the_sum)


def withdraw(name, the_sum):
    bank[name] = bank.get(name, 0) - int(the_sum)


def balance(name):
    if name not in bank:
        print('ERROR')
    else:
        print(bank[name])


def income(percent):
    for k, v in bank.items():
        if v > 0:
            bank[k] = int(v * ((int(percent) / 100) + 1))


bank = {}
with open('input.txt') as f:
    for line in f:
        line = line.split()
        if 'BALANCE' in line:
            balance(line[1])
        elif 'DEPOSIT' in line:
            deposit(line[1], line[2])
        elif 'WITHDRAW' in line:
            withdraw(line[1], line[2])
        elif 'INCOME' in line:
            income(line[1])
        else:
            withdraw(line[1], line[3])
            deposit(line[2], line[3])
