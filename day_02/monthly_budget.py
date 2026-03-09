"""Monthly budget tracker (command line).

Features:
 - ask for total monthly budget
 - prompt for three expenses per cycle
 - subtract expenses from budget and show balance
 - warn if balance drops below 500
 - allow user to repeat expense input until they type 'done' as expense name
"""

def get_float(prompt):
    while True:
        val = input(prompt).strip()
        try:
            return float(val)
        except ValueError:
            print("Please enter a valid number.")


def main():
    print("Monthly Budget Program")
    total_budget = get_float("Enter total monthly budget: ")
    balance = total_budget

    while True:
        print(f"\nCurrent balance: {balance:.2f}")
        print("Enter three expenses (or type 'done' to quit):")
        expenses = []
        for i in range(1, 4):
            entry = input(f"  Expense {i}: ").strip()
            if entry.lower() == "done":
                print("Exiting expense entry.")
                break
            try:
                expenses.append(float(entry))
            except ValueError:
                print("Invalid number, try again.")
                break
        if not expenses or entry.lower() == "done":
            break
        spent = sum(expenses)
        balance -= spent
        print(f"Spent {spent:.2f}, new balance {balance:.2f}")
        if balance < 500:
            print("Warning: Low Funds")

    print(f"\nFinal balance: {balance:.2f}")
    if balance < 500:
        print("Warning: Low Funds")
    print("Goodbye!")

if __name__ == "__main__":
    main()
