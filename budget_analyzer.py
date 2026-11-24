import csv


def analyze_expenses(filename, monthly_income):
    """
    Reads a CSV expense file, categorizes spending into Needs, Wants, and Savings,
    and evaluates financial health against the 50/30/20 budgeting rule.
    """
    totals = {"Needs": 0.0, "Wants": 0.0, "Savings": 0.0}
    total_spent = 0.0

    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                category = row["Category"].strip().capitalize()
                amount = float(row["Amount"])

                if category in totals:
                    totals[category] += amount
                else:
                    # Fallback if an unrecognized category appears
                    totals["Wants"] += amount

                total_spent += amount

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return
    except KeyError:
        print("Error: CSV file must contain 'Category' and 'Amount' columns.")
        return
    except ValueError:
        print("Error: Invalid numeric value found in 'Amount' column.")
        return

    remaining_cash = monthly_income - total_spent

    print("\n=== MONTHLY CASHFLOW & 50/30/20 BUDGET REPORT ===")
    print(f"Monthly Net Income : RM {monthly_income:,.2f}")
    print(f"Total Allocated    : RM {total_spent:,.2f}")
    print(f"Unallocated Cash   : RM {remaining_cash:,.2f}")
    print("-" * 65)
    print(f"{'Category':<12} | {'Actual (RM)':<14} | {'Actual %':<10} | {'Target %':<10} | {'Status'}")
    print("-" * 65)

    targets = {"Needs": 50.0, "Wants": 30.0, "Savings": 20.0}

    for category in ["Needs", "Wants", "Savings"]:
        actual_rm = totals[category]
        actual_pct = (actual_rm / monthly_income) * 100
        target_pct = targets[category]

        if category == "Savings":
            status = "Healthy" if actual_pct >= target_pct else "Below Target"
        else:
            status = "Healthy" if actual_pct <= target_pct else "Over Limit"

        print(f"{category:<12} | {actual_rm:<14,.2f} | {actual_pct:<9.1f}% | {target_pct:<9.0f}% | {status}")

    print("-" * 65)
    if remaining_cash < 0:
        print("Alert: Your total expenses exceed your monthly income!")
    elif totals["Savings"] / monthly_income >= 0.20:
        print("Great job! You met or exceeded the 20% savings benchmark.")
    else:
        print("Tip: Try reducing 'Wants' slightly to hit at least 20% savings.")


def main():
    print("=== PERSONAL CASHFLOW & BUDGET ANALYZER ===")
    try:
        income = float(input("Enter your monthly net income (RM): "))
        if income <= 0:
            print("Error: Monthly income must be greater than zero.")
            return

        csv_file = input("Enter expense CSV filename (press Enter for 'sample_expenses.csv'): ").strip()
        if not csv_file:
            csv_file = "sample_expenses.csv"

        analyze_expenses(csv_file, income)

    except ValueError:
        print("Input Error: Please enter a valid numeric amount for income.")


if __name__ == "__main__":
    main()
