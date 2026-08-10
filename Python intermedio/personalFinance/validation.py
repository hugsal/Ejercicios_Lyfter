from datetime import datetime


class Validation:

    @staticmethod
    def validate_amount(amount):
        if amount is None or str(amount).strip() == "":
            raise ValueError("Amount cannot be empty")
        try:
            amount_val = float(amount)
        except (ValueError, TypeError) as ex:
            raise ValueError("Amount must be a number") from ex
        if amount_val <= 0:
            raise ValueError("Amount must be greater than 0")
        return amount_val

    @staticmethod
    def validate_description(description):
        description_val = str(description).strip()
        if len(description_val) == 0:
            raise ValueError("Description cannot be empty")

        is_numeric = False
        try:
            float(description_val)
            is_numeric = True
        except (ValueError, TypeError):
            pass

        if is_numeric:
            raise ValueError("Description cannot be a number")

        return description_val

    @staticmethod
    def validate_category(category):
        if not isinstance(category, str):
            raise TypeError("Category must be a string")
        category_val = category.strip()
        if len(category_val) == 0:
            raise ValueError("Category cannot be empty")
        return category_val

    @staticmethod
    def validate_date(date):
        if date is None or str(date).strip() == "":
            raise ValueError("Date cannot be empty")
        try:
            date_val = datetime.strptime(date, "%d/%m/%Y").date()

        except (ValueError, TypeError) as ex:
            raise ValueError("Date must be in dd/mm/yyyy format") from ex

        today = datetime.now().date()

        if date_val > today:
            raise ValueError("Date cannot be in the future")

        return date_val
