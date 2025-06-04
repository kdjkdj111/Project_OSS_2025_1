import datetime
from expense import Expense
from collections import defaultdict


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

    def category_graph(self):
        if not self.expenses:
            print("지출 내역이 없습니다. 그래프를 표시할 수 없습니다.\n")
            return

        category_totals = defaultdict(int)
        for e in self.expenses:
            category_totals[e.category] += e.amount

        print("[카테고리별 지출 비율]")

        total = sum(category_totals.values())
        for cat, amt in category_totals.items():
            ratio = amt / total
            bar = '█' * int(ratio * 30) 
            print(f"{cat:10} | {bar} {amt}원 ({ratio*100:.1f}%)")

        print()
        