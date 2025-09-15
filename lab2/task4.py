names = input().split()
num_people = len(names)

spent = {name: 0 for name in names}

n = int(input())
for _ in range(n):
    line = input().split()
    person = line[0]
    amount = int(line[1])
    spent[person] += amount

total = sum(spent.values())
avg = total / num_people

balances = {name: spent[name] - avg for name in names}

debtors = []
creditors = []

for name, bal in balances.items():
    if bal < -0.001:
        debtors.append([name, -bal])
    elif bal > 0.001:
        creditors.append([name, bal])

transfers = []

i = j = 0
while i < len(debtors) and j < len(creditors):
    debtor_name, debt_amount = debtors[i]
    creditor_name, credit_amount = creditors[j]

    transfer_amount = min(debt_amount, credit_amount)

    transfers.append((debtor_name, creditor_name, round(transfer_amount, 2)))

    debtors[i][1] -= transfer_amount
    creditors[j][1] -= transfer_amount

    if abs(debtors[i][1]) < 0.001:
        i += 1
    if abs(creditors[j][1]) < 0.001:
        j += 1

print(len(transfers))
for debtor, creditor, amount in transfers:
    print(debtor, creditor, f"{amount:.2f}")
