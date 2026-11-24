def calculate_compound_interest (principal, monthly_contribution, annual_rate, years):
    """Calculates year-by-year investment growth with monthly compounding"""
    monthly_rate=(annual_rate/100)/12
    total_months=years*12
    current_balance=principal
    total_invested=principal

    print("\n---INVESTMENT GROWTH PROJECTION---")
    print(f"{'Year':<8} | {'Total Principal (RM)':<22} | {'Total Dividend (RM)':<21} | {'Ending Balance(RM)':<20}")
    print("-"*80)

    for month in range(1,total_months +1):
        current_balance = (current_balance + monthly_contribution)* (1+ monthly_rate)
        total_invested += monthly_contribution

        #Display annual summary at the end of every 12 months
        if month%12==0:
            year=month//12
            total_profit=current_balance-total_invested
            print(f"{year:<8} | {total_invested:22,.2f} | {total_profit:<21,.2f} | {current_balance:<20,.2f}")

    return current_balance, total_invested

def main():
    print("===COMPOUND INTEREST & INVESTMENT SIMULATOR ===")
    try:
        initial_principal=float(input("Enter initial investment amount (RM): "))
        monthly_savings=float(input("Enter monthly contribution (RM): "))
        annual_dividend_rate=float(input("Estimated annual dividend rate (%): "))
        investment_years=int(input("Enter investment duration (years): "))

        if initial_principal < 0 or monthly_savings < 0 or annual_dividend_rate < 0 or investment_years <= 0:
            print("Error: Please enter positive values for all inputs.")
            return

        final_balance, total_principal = calculate_compound_interest(initial_principal, monthly_savings, annual_dividend_rate, investment_years)
        net_profit = final_balance - total_principal

        print("-"*80)
        print(f"Summary After {investment_years} Years:")
        print(f"Total Principal Invested: RM {total_principal:,.2f}")
        print(f"Final Dividend Earned: RM {net_profit:,.2f}")
        print(f"Final Portfolio Value: RM {final_balance:,.2f}")

    except ValueError:
        print("Error: Invalid input. Please enter numeric values only.")

if __name__ == "__main__":
    main()
