from entities.productEntity import Product
from sqlalchemy import select


class ProductRepository:
    @staticmethod
    def format_product(product):
        if not product:
            return None
        return {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "stock": product.stock,
            "admission_date": product.admission_date.strftime("%d/%m/%Y")
            if product.admission_date
            else None,
        }

    @staticmethod
    def create_product(db, name, price, stock, description=None):
        new_product = Product(
            name=name, price=price, stock=stock, description=description
        )
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        return ProductRepository.format_product(new_product)

    @staticmethod
    def get_product_by_id(db, product_id):
        product = db.get(Product, int(product_id))
        if not product:
            return None
        return ProductRepository.format_product(product)

    @staticmethod
    def get_product_entity_by_id(db, product_id):
        return db.get(Product, int(product_id))

    @staticmethod
    def get_product_by_name(db, name):
        stmt = select(Product).where(Product.name == name)
        product = db.scalar(stmt)
        if not product:
            return None
        return ProductRepository.format_product(product)

    @staticmethod
    def get_products(db):
        stmt = select(Product)
        return list(map(ProductRepository.format_product, db.scalars(stmt).all()))

    @staticmethod
    def update_product(
        db, product_id, name=None, price=None, stock=None, description=None
    ):
        product = db.get(Product, int(product_id))
        if product:
            if name is not None:
                product.name = name
            if price is not None:
                product.price = price
            if stock is not None:
                product.stock = stock
            if description is not None:
                product.description = description
            db.commit()
            db.refresh(product)
            return ProductRepository.format_product(product)
        return None

    @staticmethod
    def subtract_stock(db, product_id, quantity):
        product = db.get(Product, int(product_id))
        if product:
            product.stock = max(0, product.stock - quantity)
            db.commit()
            db.refresh(product)
            return ProductRepository.format_product(product)
        return None

    @staticmethod
    def add_stock(db, product_id, quantity):
        product = db.get(Product, int(product_id))
        if product:
            product.stock = product.stock + quantity
            db.commit()
            db.refresh(product)
            return ProductRepository.format_product(product)
        return None

    @staticmethod
    def delete_product(db, product_id):
        product = db.get(Product, int(product_id))
        if product:
            db.delete(product)
            db.commit()
            return True
        return False
