from datetime import datetime


class Transaction:
    def __init__(self, transactions=None):
        self.transactions = transactions if transactions is not None else []

    def new_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_transactions(self):
        return self.transactions

    def get_transactions_table(self):
        data = [
            [
                transaction.get("date", ""),
                f"{'-' if transaction.get('transaction_type') == '-EXPENSE-' else ''}{transaction.get('amount', 0.0)}",
                transaction.get("description", ""),
                transaction.get("category", ""),
            ]
            for transaction in self.transactions
        ]
        sorted_data = sorted(data, key=lambda x: self.__parse_date(x[0]))
        return sorted_data

    def get_filtered_transactions_table(self, initial_date, final_date):
        return [
            [
                transaction.get("date", ""),
                f"{' - ' if transaction.get('transaction_type') == '-EXPENSE-' else ''}{transaction.get('amount', 0.0)}",
                transaction.get("description", ""),
                transaction.get("category", ""),
            ]
            for transaction in self.transactions
            if self.__parse_date(transaction.get("date", "")) >= initial_date
            and self.__parse_date(transaction.get("date", "")) <= final_date
        ]

    def get_totals(self):
        expenses = 0
        incomes = 0
        for transaction in self.transactions:
            if transaction.get("transaction_type") == "-EXPENSE-":
                expenses += float(transaction.get("amount", 0.0))
            else:
                incomes += float(transaction.get("amount", 0.0))
        total = incomes - expenses
        return self.transactions, incomes, expenses, total

    @staticmethod
    def __parse_date(date_str):
        try:
            return datetime.strptime(date_str.strip(), "%d/%m/%Y").date()
        except (ValueError, TypeError):
            return None
