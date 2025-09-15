n = int(input())

orders = []
pizza_count = {}
daily_revenue = {}
max_price = -1
max_order = None
total_sum = 0.0

for _ in range(n):
    line = input().split()
    date = line[0]
    pizza_name = line[1]
    price = float(line[2])
    orders.append((date, pizza_name, price))
    pizza_count[pizza_name] = pizza_count.get(pizza_name, 0) + 1
    daily_revenue[date] = daily_revenue.get(date, 0) + price
    if price > max_price:
        max_price = price
        max_order = (price, date, pizza_name)
    total_sum += price
print("Most popular pizzas:")
sorted_pizzas = sorted(pizza_count.items(), key=lambda x: (-x[1], x[0]))
for name, count in sorted_pizzas:
    print(name, count)
print("\nRevenue by date:")
sorted_dates = sorted(daily_revenue.keys())
for date in sorted_dates:
    print(date, f"{daily_revenue[date]:.2f}")
print(f"\nMost expensive order: {max_order[0]:.2f} on {max_order[1]}, pizza: {max_order[2]}")
avg_price = total_sum / n
print(f"\nAverage order price: {avg_price:.2f}")
'''
5
2025-04-01 Маргарита 450
2025-04-01 Пепперони 600
2025-04-02 Маргарита 470
2025-04-02 Маргарита 460
2025-04-03 Гавайская 550
'''
