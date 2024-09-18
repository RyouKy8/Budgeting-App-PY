class BudgetApp:

    def __init__(self):
        self.budget = 0
        self.expenses = []

    def set_budget(self):
        try:
            self.budget = float(input("Enter your initial budget: "))
            print(f"Budget set to: ${self.budget:.2f}")
        except ValueError:
            print("Please enter a valid number for the budget.")

    def add_expense(self):
        try:
            expense_name = input("Enter the expense description: ")
            expense_amount = float(input("Enter the expense amount: "))
            self.expenses.append({'description': expense_name, 'amount': expense_amount})
            self.budget -= expense_amount
            print(f"Expense '{expense_name}' of ${expense_amount:.2f} added.")
        except ValueError:
            print("Please enter a valid expense amount.")

    def view_expenses(self):
        if self.expenses:
            print("\nList of Expenses:")
            for idx, expense in enumerate(self.expenses, 1):
                print(f"{idx}. {expense['description']} - ${expense['amount']:.2f}")
        else:
            print("\nNo expenses added yet.")

    def check_balance(self):
        print(f"\nRemaining balance: ${self.budget:.2f}")

    def main_menu(self):
        while True:
            print("\n--- Budgeting App Menu ---")
            print("1. Set Budget")
            print("2. Add Expense")
            print("3. View Expenses")
            print("4. Check Balance")
            print("5. Exit")

            choice = input("Choose an option (1-5): ")

            if choice == '1':
                self.set_budget()
            elif choice == '2':
                self.add_expense()
            elif choice == '3':
                self.view_expenses()
            elif choice == '4':
                self.check_balance()
            elif choice == '5':
                print("Kau pergi mana njirr")
                break
            else:
                print("Invalid option. You tried to be a smartass and wasted both our time. Hope you're happy.")

if __name__ == "__main__":
    app = BudgetApp()
    app.main_menu()
