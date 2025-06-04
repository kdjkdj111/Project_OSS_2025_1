import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, date, category, description, amount):
        expense = Expense(date, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

    def search_expenses(self):
        print("\n[지출 검색 기능]")
        print("1. 날짜 범위로 검색")
        print("2. 금액 범위로 검색")
        choice = input("검색 방법을 선택하세요 > ")

        if choice == "1":
            start = input("시작 날짜 (YYYY-MM-DD 또는 today): ")
            if start.strip().lower() == "today":
                start = datetime.date.today().isoformat()
            end = input("끝 날짜 (YYYY-MM-DD 또는 today): ")
            if end.strip().lower() == "today":
                end = datetime.date.today().isoformat()
            try:
                start_date = datetime.date.fromisoformat(start)
                end_date = datetime.date.fromisoformat(end)
            except ValueError:
                print("날짜 형식이 잘못되었습니다.\n")
                return

            print(f"\n[검색 결과: {start} ~ {end}]")
            found = False
            for e in self.expenses:
                expense_date = datetime.date.fromisoformat(e.date)
                if start_date <= expense_date <= end_date:
                    print(e)
                    found = True
            if not found:
                print("해당 범위의 지출이 없습니다.\n")

        elif choice == "2":
            try:
                min_price = int(input("최소 금액: "))
                max_price = int(input("최대 금액: "))
            except ValueError:
                print("금액을 숫자로 입력해주세요.\n")
                return

            print(f"\n[검색 결과: {min_price}원 ~ {max_price}원]")
            found = False
            for e in self.expenses:
                if min_price <= e.amount <= max_price:
                    print(e)
                    found = True
            if not found:
                print("해당 금액 범위의 지출이 없습니다.\n")

        else:
            print("잘못된 선택입니다.\n")
