#a function that calculates discount
def calculate_discount(price, discount_percent):
    """Calculate the final price after applying a discount if the discount is 20% or more."""
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    else:
        return price

# Main program logic
def main():
    # Get user input
    price = float(input("Please input the original price of the item: "))
    discount_percent = float(input("Input a percentage discount: "))

    # Calculate the final price
    final_price = calculate_discount(price, discount_percent)

    # Print the result
    if discount_percent >= 20:
        print(f"The discounted price is: {final_price:.2f}")
    else:
        print(f"No discount applied, your price is: {price:.2f}")

if __name__ == "__main__":
    main()
