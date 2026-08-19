import csv
import os


class Data:
    def __init__(self, filepath="transactions.csv"):
        self.filepath = filepath
        self.data = []
        if os.path.exists(self.filepath):
            try:
                with open(self.filepath, "r", encoding="utf-8") as file:
                    reader = csv.DictReader(file)
                    self.data = [row for row in reader if row]
            except Exception:
                self.data = []
        else:
            dir_name = os.path.dirname(self.filepath)
            if dir_name:
                os.makedirs(dir_name, exist_ok=True)
            with open(self.filepath, "w", encoding="utf-8") as file:
                pass

    def get_transactions(self):
        return self.data

    def get_categories(self):
        categories = []
        for transaction in self.data:
            category = transaction.get("category")
            if category:
                cleaned = category.strip().capitalize()
                if cleaned not in categories:
                    categories.append(cleaned)
        return categories

    def save_data(self, transactions):
        if not transactions:
            with open(self.filepath, "w", encoding="utf-8") as file:
                pass
            return True

        with open(self.filepath, "w", encoding="utf-8") as file:
            headers = list(transactions[0].keys())
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(transactions)
        return True

    def export_to_csv(
        self, transactions, incomes, expenses, total, filepath="balance.csv"
    ):
        if not transactions:
            return False

        try:
            with open(filepath, "w", newline="", encoding="utf-8") as csvfile:
                headers = list(transactions[0].keys())
                writer = csv.DictWriter(
                    csvfile, fieldnames=headers, extrasaction="ignore"
                )
                writer.writeheader()
                writer.writerows(transactions)

                csvfile.write("\n")
                summary_writer = csv.writer(csvfile)
                summary_writer.writerow(["Totales", "Valor"])
                summary_writer.writerow(["Ingresos", incomes])
                summary_writer.writerow(["Gastos", expenses])
                summary_writer.writerow(["Balance neto", total])
        except (OSError, IOError):
            return False

        return True
