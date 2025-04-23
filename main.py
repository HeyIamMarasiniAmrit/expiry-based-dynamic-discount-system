from datetime import datetime
from datetime import datetime, timedelta

def days_until_expiry(expiry_date, current_date=None):
    current_date = current_date or datetime.now()
    delta = expiry_date - current_date
    return max(delta.days, 0)


def get_discount_percentage(days_left, max_days, max_discount):
    # Decreases discount as time increases
    return min((1 - (days_left / max_days)) * max_discount, max_discount)

def discount_by_expiry(days_left):
    if days_left > 10:
        return 5  # 5% discount
    elif days_left > 5:
        return 15
    elif days_left > 2:
        return 30
    elif days_left > 0:
        return 50
    else:
        return 80  # expires today or expired

def discounted_price(base_price, discount_percent):
    return round(base_price * (1 - discount_percent / 100), 2)



expiry = datetime.now() + timedelta(days=5)  # example expiry
base_price = 100

days_left = days_until_expiry(expiry)
discount = discount_by_expiry(days_left)
price = discounted_price(base_price, discount)

print(f"Days Left: {days_left}, Discount: {discount}%, Price: ${price}")

