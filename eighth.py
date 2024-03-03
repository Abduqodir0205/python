class ATM:
    def __init__(self, password, balance=0):
        self.password = password
        self.balance = balance

    def authenticate(self, entered_password):
        return entered_password == self.password

    def view_balance(self):
        print(f"Joriy balans: ${self.balance}")

    def top_up_balance(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} muvaffaqiyatli qo'shildi.")
        else:
            print("Noto'g'ri miqdor. Iltimos, musbat qiymat kiriting.")

    def withdraw_money(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Naqd pul muvaffaqiyatli yechildi. ${amount} joriy balansdan ayrildi.")
        else:
            print("Yetarli mablag' yoki noto'g'ri yechim miqdori.")

if __name__ == "__main__":
    atm_password = input(" parolni kiriting: ")

    my_atm = ATM(password=atm_password, balance=1000)

    entered_password = input("parolini qayta kiriting: ")
    if my_atm.authenticate(entered_password):
        print("Autentifikatsiya muvaffaqiyatli. ATM'ga xush kelibsiz!")

        print("1. Balansni ko'rish")
        print("2. Balansni to'ldirish")
        print("3. Naqd pulni yechish")

        try:
            choice = int(input("Tanlovni kiriting (1/2/3): "))

            if choice not in [1, 2, 3]:
                raise ValueError("Noto'g'ri tanlov. Iltimos, 1, 2 yoki 3 ni kiriting.")

            if choice == 1:
                my_atm.view_balance()
            elif choice == 2:
                amount_to_top_up = float(input("To'lash uchun miqdorni kiriting: $"))
                my_atm.top_up_balance(amount_to_top_up)
            elif choice == 3:
                amount_to_withdraw = float(input("Naqd pulni yechish uchun miqdorni kiriting: $"))
                my_atm.withdraw_money(amount_to_withdraw)

        except ValueError as e:
            print(f"Xato: {e}. Iltimos, to'g'ri tanlov kiriting.")
    else:
        print("Autentifikatsiya muvaffaqiyatsiz. Chiqilmoqda.")
