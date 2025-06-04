import datetime
from expense import Expense

class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
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

    def save_history(self, filepath):
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                for e in self.expenses:
                    line = f"{e.date},{e.category},{e.description},{e.amount}\n"
                    f.write(line)
            print("지출 내역이 성공적으로 저장되었습니다.\n")
        except Exception as e:
            print(f"저장 중 오류 발생: {e}")

    def load_history(self, filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                for line in f:
                    parts = line.strip().split(',')
                    if len(parts) != 4:
                        print(f"형식 오류: {line.strip()}")
                        continue
                    date_str, category, description, amount_str = parts
                    try:
                        amount = int(amount_str)
                        expense = Expense(date_str, category, description, amount)
                        self.expenses.append(expense)
                    except ValueError:
                        print(f"숫자 변환 오류: {amount_str}")
            print("지출 파일이 성공적으로 불러와졌습니다.\n")
        except FileNotFoundError:
            print("파일을 찾을 수 없습니다.\n")


