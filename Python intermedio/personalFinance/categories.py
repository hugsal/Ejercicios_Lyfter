class Categories:
    def __init__(self, categories=None):
        self.categories = categories if categories is not None else []

    def new_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def get_categories(self):
        return self.categories
