from bank import Bank
from exceptions import (
    AccountNotFoundError,
    InsufficientFundsError,
    InvalidAmountError,
)


def main():
    bank = Bank()

    while True:
        print("\n========== PunasBank ==========")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Close Account")
        print("6. Exit")
        print("================================")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                name = input("Enter customer name: ")
                account = bank.create_account(name)

                print("\nAccount Created Successfully!")
                print(f"Account ID : {account.account_id}")
                print(f"Customer   : {account.customer_name}")
                print(f"Balance    : ₹{account.balance:.2f}")

            elif choice == "2":
                account_id = int(input("Enter Account ID: "))
                amount = float(input("Enter Deposit Amount: "))

                bank.deposit(account_id, amount)
                print("Deposit Successful!")

            elif choice == "3":
                account_id = int(input("Enter Account ID: "))
                amount = float(input("Enter Withdrawal Amount: "))

                bank.withdraw(account_id, amount)
                print("Withdrawal Successful!")

            elif choice == "4":
                account_id = int(input("Enter Account ID: "))
                balance = bank.check_balance(account_id)

                print(f"Current Balance: ₹{balance:.2f}")

            elif choice == "5":
                account_id = int(input("Enter Account ID: "))

                bank.close_account(account_id)
                print("Account Closed Successfully!")

            elif choice == "6":
                print("\nThank you for using PunasBank!")
                break

            else:
                print("Invalid Choice!")

        except (
            AccountNotFoundError,
            InsufficientFundsError,
            InvalidAmountError,
        ) as e:
            print(f"Error: {e}")

        except ValueError:
            print("Invalid input! Please enter numbers where required.")


if __name__ == "__main__":
    main()