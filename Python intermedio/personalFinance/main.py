from data import Data
from transaction import Transaction
from categories import Categories
from view import FinanceView
from presenter import FinancePresenter


def main():
    data = Data()
    transaction = Transaction(data.get_transactions())
    categories = Categories(data.get_categories())
    view = FinanceView()
    presenter = FinancePresenter(view, transaction, categories, data)
    presenter.run()


if __name__ == "__main__":
    main()
