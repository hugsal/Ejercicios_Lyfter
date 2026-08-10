import FreeSimpleGUI as sg


class FinanceView:
    def __init__(self):
        self.main_window_instance = None

    def show_main_window(self, transactions_table_data):
        layout = [
            [sg.Text("Transactions")],
            [
                sg.Text("Initial date:"),
                sg.Input(key="-INITIAL_DATE-", size=(15, 1)),
                sg.Text("Final date:"),
                sg.Input(key="-FINAL_DATE-", size=(15, 1)),
                sg.Button("filter", key="-FILTER-"),
                sg.Button("clear filter", key="-CLEAR_FILTER-"),
            ],
            [
                sg.Button("New Category", key="-CATEGORY-"),
                sg.Button("Export CSV", key="-EXPORT_CSV-"),
            ],
            [
                sg.Table(
                    values=transactions_table_data,
                    headings=["Date", "Amount", "Description", "Category"],
                    key="-TRANSACTIONS-",
                    alternating_row_color="#eef2f3",
                    background_color="#ffffff",
                    text_color="#2c3e50",
                    header_background_color="#1a365d",
                    header_text_color="#ffffff",
                    row_height=26,
                    auto_size_columns=False,
                    col_widths=[12, 10, 25, 15],
                    justification="center",
                    num_rows=12,
                    display_row_numbers=False,
                ),
            ],
            [
                sg.Button("New Expense", key="-EXPENSE-"),
                sg.Button("New Income", key="-INCOME-"),
            ],
        ]
        self.main_window_instance = sg.Window("Personal Finance", layout)

    def read_event(self):
        if self.main_window_instance:
            return self.main_window_instance.read()
        return None, None

    def update_transactions_table(self, transactions_table_data):
        if self.main_window_instance:
            self.main_window_instance["-TRANSACTIONS-"].update(transactions_table_data)

    def clear_date_inputs(self):
        if self.main_window_instance:
            self.main_window_instance["-INITIAL_DATE-"].update("")
            self.main_window_instance["-FINAL_DATE-"].update("")

    def show_new_transaction_window(self, categories, transaction_event):
        message = "New expense" if transaction_event == "-EXPENSE-" else "New income"
        layout = [
            [sg.Text("Description"), sg.Input(key="-DESCRIPTION-")],
            [sg.Text("Amount"), sg.Input(key="-AMOUNT-")],
            [sg.Text("Date"), sg.Input(key="-DATE-")],
            [
                sg.Text("Category"),
                sg.Combo(categories, key="-CATEGORY-"),
            ],
            [sg.Button("Save", key="-SAVE-"), sg.Button("Cancel", key="-CANCEL-")],
        ]
        window = sg.Window(message, layout, modal=True)
        transaction_values = None

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "-CANCEL-"):
                break
            elif event == "-SAVE-":
                transaction_values = values
                break

        window.close()
        return transaction_values

    def show_new_category_window(self):
        layout = [
            [sg.Text("New Category")],
            [sg.Input(key="-CATEGORY-")],
            [sg.Button("Save", key="-SAVE-"), sg.Button("Cancel", key="-CANCEL-")],
        ]
        window = sg.Window("New Category", layout, modal=True)
        category_val = None

        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "-CANCEL-"):
                break
            elif event == "-SAVE-":
                category_val = values["-CATEGORY-"]
                break

        window.close()
        return category_val

    def show_error(self, message):
        sg.popup(message)

    def close(self):
        if self.main_window_instance:
            self.main_window_instance.close()
            self.main_window_instance = None
