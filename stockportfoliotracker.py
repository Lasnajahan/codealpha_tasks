# Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420,
    "AMZN": 190
}

total_investment = 0

print("===== Stock Portfolio Tracker =====")
print("\nAvailable stocks:")

for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

num_stocks = int(input("\nHow many different stocks do you want to buy? "))

portfolio = []

for i in range(num_stocks):
    stock = input("\nEnter stock symbol: ").upper()

    if stock not in stock_prices:
        print("Stock not available. Please try again.")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        continue

    investment = stock_prices[stock] * quantity
    total_investment += investment

    portfolio.append((stock, quantity, investment))

print("\n===== Your Portfolio =====")

for stock, quantity, investment in portfolio:
    print(
        f"{stock} | Quantity: {quantity} | "
        f"Investment: ${investment:.2f}"
    )

print(f"\nTotal Investment: ${total_investment:.2f}")

# Save the result to a text file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Tracker\n")
    file.write("=======================\n")

    for stock, quantity, investment in portfolio:
        file.write(
            f"{stock} | Quantity: {quantity} | "
            f"Investment: ${investment:.2f}\n"
        )

    file.write(f"\nTotal Investment: ${total_investment:.2f}\n")

print("\nPortfolio saved to portfolio.txt")