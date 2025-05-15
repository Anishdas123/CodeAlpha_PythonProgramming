import yfinance as yf

portfolio = {}

def is_valid_symbol(symbol):
    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d")
        return not data.empty
    except:
        return False

def add_stock(symbol, quantity, purchase_price):
    symbol = symbol.upper()
    if not is_valid_symbol(symbol):
        print(f"'{symbol}' is not a valid stock symbol or data is unavailable.\n")
        return

    portfolio[symbol] = {
        'quantity': quantity,
        'purchase_price': purchase_price
    }
    print(f"✅ Added {quantity} shares of {symbol} at ${purchase_price:.2f} each.\n")

def remove_stock(symbol):
    symbol = symbol.upper()
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"🗑️ Removed {symbol} from portfolio.\n")
    else:
        print(f"⚠️ {symbol} not found in portfolio.\n")

def get_current_price(symbol):
    try:
        stock = yf.Ticker(symbol)
        data = stock.history(period="1d")
        if not data.empty:
            return data['Close'][-1]
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
    return None

def view_portfolio():
    if not portfolio:
        print("📂 Portfolio is empty.\n")
        return

    total_value = 0
    total_cost = 0
    print("\n📊 Current Portfolio:")
    print("-" * 60)
    for symbol, info in portfolio.items():
        current_price = get_current_price(symbol)
        if current_price is None:
            print(f"⚠️ Could not fetch price for {symbol}\n")
            continue

        quantity = info['quantity']
        purchase_price = info['purchase_price']
        market_value = current_price * quantity
        cost_basis = purchase_price * quantity
        gain_loss = market_value - cost_basis

        total_value += market_value
        total_cost += cost_basis

        print(f"{symbol} - {quantity} shares")
        print(f"  Purchase Price: ${purchase_price:.2f}")
        print(f"  Current Price:  ${current_price:.2f}")
        print(f"  Market Value:   ${market_value:.2f}")
        print(f"  Gain/Loss:      ${gain_loss:.2f}\n")

    print("-" * 60)
    print(f"💰 Total Investment: ${total_cost:.2f}")
    print(f"📈 Total Value:      ${total_value:.2f}")
    print(f"📉 Overall Gain/Loss: ${total_value - total_cost:.2f}\n")

def menu():
    while True:
        print("📌 Stock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            symbol = input("Enter stock symbol: ").strip().upper()
            if not symbol:
                print("⚠️ Stock symbol cannot be empty.\n")
                continue
            try:
                quantity = int(input("Enter number of shares: "))
                purchase_price = float(input("Enter purchase price per share: "))
                add_stock(symbol, quantity, purchase_price)
            except ValueError:
                print("⚠️ Invalid quantity or price. Try again.\n")

        elif choice == '2':
            symbol = input("Enter stock symbol to remove: ").strip()
            remove_stock(symbol)

        elif choice == '3':
            view_portfolio()

        elif choice == '4':
            print("👋 Exiting portfolio tracker. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Please choose 1-4.\n")

if __name__ == "__main__":
    menu()
