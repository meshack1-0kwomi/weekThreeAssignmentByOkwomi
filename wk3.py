def calculate_discount(price, discount_percent):
    if discount_percent >= 0.20:
        final_price = price - (price * discount_percent)
    else:
        final_price = price
    return final_price
price = int(input("Enter the price of the product: "))   
discount_percent = float(input("Enter the discount marked on the product: "))   
print(calculate_discount(price, discount_percent))