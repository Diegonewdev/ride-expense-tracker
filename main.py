import csv
from datetime import datetime

# Arquivo CSV onde os dados serão salvos
FILENAME = "expenses.csv"

def add_expense(date, fuel_type, liters, price_per_liter, km, earnings):
    """Adiciona um novo gasto ao arquivo CSV"""
    cost = liters * price_per_liter
    cost_per_km = cost / km if km > 0 else 0
    net = earnings - cost

    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, fuel_type, liters, price_per_liter, km, earnings, cost, cost_per_km, net])

    print(f"✔ Expense added: {fuel_type}, {liters}L, {km} km, R${cost:.2f}, Net: R${net:.2f}")

def init_csv():
    """Cria o arquivo CSV com cabeçalhos, se não existir"""
    try:
        with open(FILENAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["date", "fuel_type", "liters", "price_per_liter", "km", "earnings", "cost", "cost_per_km", "net"])
    except FileExistsError:
        pass

def main():
    print("🚗 Ride Expense Tracker")
    init_csv()

    date = datetime.now().strftime("%Y-%m-%d")
    fuel_type = input("Fuel type (ethanol/gasoline): ")
    liters = float(input("Liters filled: "))
    price_per_liter = float(input("Price per liter: "))
    km = float(input("Kilometers driven: "))
    earnings = float(input("Total earnings of the day: "))

    add_expense(date, fuel_type, liters, price_per_liter, km, earnings)

if __name__ == "__main__":
    main()
feat: add initial Python script to log expenses
