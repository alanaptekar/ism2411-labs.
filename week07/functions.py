# AI Disclosure

def calculate_tax(price, rate):
    return price * rate

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)
print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")
print(f"Tax on $350 at 5%: ${calculate_tax(350, 0.05):.2f}")
# --- Exercise 1 ---

def apply_discount(price, tier):
    if tier == "gold":
        discount = 0.15
    elif tier == "silver":
        discount = 0.10
    elif tier == "bronze":
        discount = 0.05
    else:
        return price 
        
    return price * (1 - discount)

original_price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    discounted_price = apply_discount(original_price, tier)
    print(f"{tier}: ${discounted_price:.2f}")

# --- Exercise 2 ---

def apply_discount(price, discount_tier):
    if discount_tier.lower() == "gold":
        return price * 0.85
    else:
        return price
def add_tax(price, tax_rate):
    return price * (1 + tax_rate)

def final_price(price, discount_tier, tax_rate):
    discounted_price = apply_discount(price, discount_tier)
    total_price = add_tax(discounted_price, tax_rate)
    return total_price

start_price = 200
discount_tier = "gold"
tax = 0.07

gold_price = apply_discount(start_price, discount_tier)
print(f"After gold discount: ${gold_price:.2f}")

taxed_price = add_tax(gold_price, tax)
print(f"After tax: ${taxed_price:.2f}")

result = final_price(start_price, discount_tier, tax)
print(f"final_price({start_price}, \"{discount_tier}\", {tax}) = ${result:.2f}")

# --- Exercise 3 ---

print(f"final_price(200, 0.07, 'gold') = ${final_price(200, 'gold', 0.07):.2f}")
        

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, discount_tier in orders:
    total = final_price(price, discount_tier, 0.07)
    print(f"Price: ${price} | Discount Tier: {discount_tier} | Final: ${total:.2f}")

# --- Exercise 4 ---

x = 100   # global variable

def double_it():
    x = 999   # local variable — different from global x!
    return x * 2

print(x)           
print(double_it()) 
print(x)           

""" First print is 100, second is 1998, third does not change and prints 100"""

# --- Exercise 6 ---

""" I found the first mistake in the code by printing the values of the variables. It gave me
insight on where to change it and I figured out what the issue is by guessing. It tells me I
should learn more and be more efficient in my approach."""
""" The code apply_discount(price, tier) is a code that breaks down the inputs (price, tier) into
percentages based on the customer's tier and how much they paid. It returns the discounted price. 
I think a colleague can use it, the code is very self explanatory."""
""" I think I use AI 50/50, it often helps me explain concepts but sometimes I use it to
finish the code quicker. I think I need to use it more strategically."""