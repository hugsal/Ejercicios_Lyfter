import pytest
from unittest.mock import Mock, patch, mock_open
from validation import Validation
from transaction import Transaction
from categories import Categories
from data import Data
from presenter import FinancePresenter


# =====================================================================
# Validation Tests
# =====================================================================


def test_validate_amount_valid():
    assert Validation.validate_amount("10.5") == 10.5
    assert Validation.validate_amount(100) == 100.0


def test_validate_amount_invalid_values():
    with pytest.raises(ValueError):
        Validation.validate_amount("-5")
    with pytest.raises(ValueError):
        Validation.validate_amount("0")
    with pytest.raises(ValueError):
        Validation.validate_amount("abc")
    with pytest.raises(ValueError):
        Validation.validate_amount("")
    with pytest.raises(ValueError):
        Validation.validate_amount(None)


def test_validate_description_valid():
    assert Validation.validate_description("Lunch") == "Lunch"
    assert Validation.validate_description("  Groceries  ") == "Groceries"


def test_validate_description_invalid():
    with pytest.raises(ValueError):
        Validation.validate_description("")
    with pytest.raises(ValueError):
        Validation.validate_description("   ")
    with pytest.raises(ValueError):
        Validation.validate_description("123")
    with pytest.raises(ValueError):
        Validation.validate_description("45.6")
    with pytest.raises(ValueError):
        Validation.validate_description("-10")


def test_validate_category_valid():
    assert Validation.validate_category("Food") == "Food"


def test_validate_category_invalid():
    with pytest.raises(ValueError):
        Validation.validate_category("")
    with pytest.raises(TypeError):
        Validation.validate_category(None)


# =====================================================================
# Model Tests (Transaction & Categories)
# =====================================================================


def test_transaction_mutable_default():
    t1 = Transaction()
    t2 = Transaction()
    t1.new_transaction({"amount": 10})
    assert len(t1.get_transactions()) == 1
    assert len(t2.get_transactions()) == 0


def test_categories_mutable_default():
    c1 = Categories()
    c2 = Categories()
    c1.new_category("Food")
    assert len(c1.get_categories()) == 1
    assert len(c2.get_categories()) == 0


def test_categories_no_duplicates():
    c = Categories(["Food"])
    c.new_category("Food")
    assert c.get_categories() == ["Food"]


# =====================================================================
# Data / Persistence Tests (Using Mock Files / builtins.open)
# =====================================================================


@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data="date,amount,description,category,transaction_type\n2026-06-24,10.5,Lunch,Food,-EXPENSE-\n",
)
@patch("os.path.exists", return_value=True)
def test_data_load_success(mock_exists, mock_file):
    data_manager = Data("dummy.csv")
    txs = data_manager.get_transactions()

    assert len(txs) == 1
    assert txs[0]["description"] == "Lunch"
    assert data_manager.get_categories() == ["Food"]
    mock_file.assert_called_once_with("dummy.csv", "r", encoding="utf-8")


@patch("builtins.open", new_callable=mock_open)
@patch("os.path.exists", return_value=False)
def test_data_save_empty(mock_exists, mock_file):
    data_manager = Data("dummy.csv")
    assert data_manager.save_data([]) is True
    mock_file.assert_called_with("dummy.csv", "w", encoding="utf-8")
