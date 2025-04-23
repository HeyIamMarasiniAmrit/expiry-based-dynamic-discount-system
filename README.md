expiry-based dynamic discount system 
.

💡 What is the problem?
You want to dynamically change the discount of a product based on how close it is to its expiry date. The goal is to sell the product before it expires — and maximize revenue or reduce waste.

 Step-by-Step Plan to Solve It
 
Understand Input Variables
You'll need data like:

expiry_date: When the product expires.

current_date: Today’s date.

base_price: Original price of the product.

min_discount, max_discount: Boundaries for the discount percentage.

Optional: Product category, demand, stock levels.

Use Cases
Supermarkets reducing prices of near-expiry goods

SaaS trials expiring

Event tickets nearing the event date

Flash sales

Bonus Add-ons
Integrate with inventory: Higher stock + close expiry = steeper discount.

Integrate with demand prediction: Slow-moving items get more aggressive discounts.

Display: "Only 2 days left — 50% off!" for marketing appeal.

# 🕒 Expiry-Based Dynamic Discount System

This project implements a dynamic discounting engine that automatically applies discounts to products based on how close they are to their expiry date. It's ideal for e-commerce, retail, inventory management systems, and platforms selling time-sensitive goods.

## 🚀 Features

- Calculates remaining days until expiry.
- Applies dynamic discounts using linear or step-based logic.
- Automatically adjusts price based on expiry date.
- Easy to integrate with any backend (Flask, Django, etc.).
- Customizable discount rules and pricing strategies.

## 📦 Use Cases

- Supermarkets & grocery stores managing perishable goods
- SaaS platforms offering time-limited trials
- Event ticketing platforms
- Pharmacies and medicine retailers
- Flash sales for aging inventory

## 🧠 How It Works

### 1. Input:
- `base_price`: Original price of the product
- `expiry_date`: Product expiry date

### 2. Processing:
- Calculates `days_left = expiry_date - current_date`
- Applies discount logic:
  - Linear formula or
  - Step-based discount rates

### 3. Output:
- Final discounted price

### Example:
```python
from datetime import datetime, timedelta
from discount_engine import days_until_expiry, discount_by_expiry, discounted_price

expiry = datetime.now() + timedelta(days=5)
base_price = 100

days_left = days_until_expiry(expiry)
discount = discount_by_expiry(days_left)
price = discounted_price(base_price, discount)

print(f"Discounted Price: ${price}")


![Image](https://github.com/user-attachments/assets/dab5563e-9ef3-434f-ac74-4445f0becf5f)
