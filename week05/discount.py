total = float(input("Enter cart total: $"))

if total >= 500:
    discount = 0.15
elif total >= 200:
    discount = 0.10
elif total >= 100:
    discount = 0.05
else:
    discount = 0   

final = total * (1 - discount)
print(f"Discount: {discount*100:.0f}%")
print(f"Final total: ${final:,.2f}")

# --- Exercise 1 ---

if final > 1000:
    status = "manager_approval_required"
else:
    status = "auto_approved"
print(f"Status: {status}")

# --- Exercise 2 ---

region = "South"
total = 250
discount = 10

if region == "South" and total >= 250:
    print("Region bonus applied: additional 2% off")
    discount += 2
else:
    print("Standard discount applied")

final_discount_decimal = discount / 100
final_price = total * (1 - final_discount_decimal)

print(f"Final discount: {discount}%")
print(f"Final price: ${final_price:,.2f}")

# --- Exercise 3 ---

customer_type = "wholesale"
if region == "South" and total >= 100 and customer_type =="wholesale":
    extra_discount = 0.03

# --- Exercise 4 ---

def flag_anomaly(amount):
    if amount <= 0:
        print("SUSPICIOUS")
    elif 1 <= amount <= 9999:
        print("NORMAL")
    elif amount >= 10000:
        print("LARGE — REVIEW REQUIRED")

test_values = [-50, 500, 15000]

for val in test_values:
    print(f"Amount: {val:6} -> ", end="")
    flag_anomaly(val)

# --- Exercise 5 ---

total_spent_this_year = 2500
orders_this_year = 6
has_outstanding_balance = False


if (total_spent_this_year > 2000 or orders_this_year > 10) and not has_outstanding_balance:
    vip_upgrade = True
else:
    vip_upgrade = False

print(f"VIP upgrade: {vip_upgrade}")

# --- Exercise 6 ---

""" If I put discount to 350, it would get the .10 discount rate. Since it is under 500 but
larger than 200, it falls into the 10% discount category."""
"""The difference between the first line and the second line is just the cleanliness of the code, 
both still have the same outcome but the second line is more readable and easier to understand."""
"""A day to day example of tiered logic is shipping fees, where usually paying more money equals
lower shipping like else, elif and if statements. Python shows me how I could implement these 
statements if I worked in this field"""