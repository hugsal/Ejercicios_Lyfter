from datetime import datetime
from validation import Validation


class FinancePresenter:
    def __init__(self, view, transaction, categories, data):
        self.view = view
        self.transaction = transaction
        self.categories = categories
        self.data = data

    def run(self):
        self.view.show_main_window(self.transaction.get_transactions_table())
        while True:
            event, values = self.view.read_event()
            if event is None:
                break

            if event in ("-EXPENSE-", "-INCOME-"):
                self.handle_new_transaction(event)
            elif event == "-FILTER-":
                self.handle_filter(
                    {
                        "initial_date": values.get("-INITIAL_DATE-"),
                        "final_date": values.get("-FINAL_DATE-"),
                    }
                )
            elif event == "-CLEAR_FILTER-":
                self.handle_clear_filter()
            elif event == "-EXPORT_CSV-":
                self.handle_export_csv()
            elif event == "-CATEGORY-":
                self.handle_new_category()

        self.view.close()

    def handle_clear_filter(self):
        self.view.update_transactions_table(self.transaction.get_transactions_table())
        self.view.clear_date_inputs()

    def handle_filter(self, values):
        try:
            initial_date = Validation.validate_date(values.get("initial_date"))
            final_date = Validation.validate_date(values.get("final_date"))
        except (ValueError, TypeError) as ex:
            self.view.show_error(str(ex))
            return
        self.view.update_transactions_table(
            self.transaction.get_filtered_transactions_table(initial_date, final_date)
        )

    def handle_new_transaction(self, transaction_event):
        categories_list = self.categories.get_categories()
        values = self.view.show_new_transaction_window(
            categories_list, transaction_event
        )
        if not values:
            return

        try:
            amount = Validation.validate_amount(values.get("-AMOUNT-"))
            description = Validation.validate_description(values.get("-DESCRIPTION-"))
            category = Validation.validate_category(values.get("-CATEGORY-"))
            date_str = values.get("-DATE-")
            if date_str:
                date = Validation.validate_date(date_str)
            else:
                date = datetime.now()
            date = date.strftime("%d/%m/%Y")
        except (ValueError, TypeError) as ex:
            self.view.show_error(str(ex))
            return

        new_tx = {
            "date": date,
            "amount": amount,
            "description": description,
            "category": category,
            "transaction_type": transaction_event,
        }

        self.transaction.new_transaction(new_tx)
        self.view.update_transactions_table(self.transaction.get_transactions_table())
        self.data.save_data(self.transaction.get_transactions())

    def handle_new_category(self):
        category_raw = self.view.show_new_category_window()
        if category_raw is None:
            return

        try:
            category = Validation.validate_category(category_raw)
        except (ValueError, TypeError) as ex:
            self.view.show_error(str(ex))
            return

        category_clean = category.strip().capitalize()
        if category_clean not in self.categories.get_categories():
            self.categories.new_category(category_clean)

    def handle_export_csv(self):
        self.data.export_to_csv(*self.transaction.get_totals())
