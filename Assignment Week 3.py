# Python code to implement the calculate_discount function and prompt the user for input

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        # Apply discount
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        # Return original price if discount is less than 20%
        return price

# Prompt user for input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price using the function
final_price = calculate_discount(price, discount_percent)

# Print the final price
if final_price != price:
    print(f"The final price after applying the discount is: {final_price}")
else:
    print(f"No discount applied. The original price is: {final_price}")
