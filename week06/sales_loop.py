sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0  

for sale in sales:
    total += sale  

print(f"Total: ${total}")

# --- Exercise 1 ---

prices = [100, 200, 150, 250, 175, 225, 125, 170]

total = 0
count = 0

for price in prices:
    total += price
    count += 1

average = total / count

print(f"Total: ${total}")
print(f"Count: {count}")
print(f"Average: ${average:.2f}")

# --- Exercise 2 ---

sales = [150, 280, 410, 95, 320]

current_max = 0

for sale in sales:
    if sale > current_max:
        current_max = sale

print(f"Largest sale: ${current_max}")
sales = [150, 280, 410, 95, 320]

current_max = 0

for sale in sales:
    if sale > current_max:
        current_max = sale

print(f"Largest sale: ${current_max}")

# --- Exercise 3 ---

sales = [50, 200, 80, 250, 100, 300, 120, 300, 45]

sales_count = 0
sales_total = 0

for sale in sales:
    
    if sale > 100:
        sales_count += 1      # Increment the counter
        sales_total += sale    # Add the sale to the total

print(f"Sales over $100: {sales_count}")
print(f"Total of those sales: ${sales_total}")

# --- Exercise 4 ---

sales = [120, 250, 75, 175, 410, 300]

for sale in sales:
    if sale > 400:
        print(f"Alert: outlier found – ${sale}. Stopping.")
        break
        

    if sale <= 100:
        continue
        
    print(f"${sale}")

# --- Exercise 5 ---

sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0
i = 0          

while i < len(sales):
    total += sales[i]
    i += 1

print(f"Total: ${total}")

"""I would use excercise 1 due to the code being shorter while producing the same result."""

# --- Exercise 6 ---

sales = [120, 80, 250, 150, 300]

for sale in sales:

    if sale >= 200:
        discount_percent = 10
    elif sale >= 100:
        discount_percent = 5
    else:
        discount_percent = 0
        
    discounted_price = sale * (1 - discount_percent / 100)
    
    print(f"${sale} -> {discount_percent}% discount -> ${discounted_price:.2f}")

# --- Exercise 7 ---
