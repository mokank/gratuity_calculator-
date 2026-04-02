import math

def calculate_gratuity():
    print("-" * 30)
    print("GRATUITY CALCULATOR (Legacy vs Statutory)")
    print("-" * 30)

    try:
        # 1. Get User Input
        basic_salary = float(input("Enter your Monthly Basic Salary (₹): "))
        years = int(input("Enter completed years of service: "))
        months = int(input("Enter remaining months of service (0-11): "))

        # 2. Tenure Rounding Logic
        # Under the Act, > 6 months rounds up to the next year.
        if months > 6:
            calc_tenure = years + 1
            print(f"\n* Tenure rounded up to {calc_tenure} years (since months > 6)")
        else:
            calc_tenure = years
            print(f"\n* Tenure calculated as {calc_tenure} years")

        # 3. Define Constants & Formulas
        service_factor = 15 / 26
        
        # Wages are 80% of Base; Basic is 40% of Base. 
        # Therefore, Statutory Wages = 2 * Basic
        wages_statutory = basic_salary * 2

        # Formula A: Legacy Policy
        payout_a = service_factor * calc_tenure * basic_salary

        # Formula B: Statutory Calculation (Capped at 20L)
        raw_statutory = service_factor * calc_tenure * wages_statutory
        payout_b = min(raw_statutory, 2000000)

        # 4. Determine Final Payout
        final_payout = max(payout_a, payout_b)

        # 5. Display Results
        print("\n" + "=" * 30)
        print(f"{'Calculation Component':<25} | {'Amount':<15}")
        print("-" * 43)
        print(f"{'Legacy Payout (A)':<25} | ₹{payout_a:,.2f}")
        print(f"{'Statutory Payout (B)':<25} | ₹{payout_b:,.2f}")
        print("-" * 43)
        print(f"{'FINAL PAYOUT (Higher)':<25} | ₹{final_payout:,.2f}")
        print("=" * 30)
        
        if raw_statutory > 2000000:
            print("Note: The statutory payout (B) was capped at the ₹20,00,000 limit.")

    except ValueError:
        print("\nError: Please enter valid numbers for salary and tenure.")

if __name__ == "__main__":
    calculate_gratuity()
