# 과제 3
# 0
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# 1
total_price = 0

# 2
for a in range(len(prices)):
    total_price += prices[a]

print(total_price)

# 3
average_price = total_price / len(prices)

# 4
print("Average price is", average_price)

# 5
new_prices = [a - 5 for a in prices]

# 6
print(new_prices)

# 7
total_revenue = 0

# 8 ~ 9
for a in range(len(hairstyles)):
    total_revenue += prices[a] * last_week[a]

# 10
print(total_revenue)

# 11
average_daily_revenue = total_revenue/7
print("Average daily revenue is", average_daily_revenue)

# 12
cuts_under_30 = [hairstyles[a] for a in range(len(new_prices)-1) if new_prices[a]<30]

# 13
print(cuts_under_30)