from entities.fruitEntity import Fruit
from sqlalchemy import select


class FruitRepository:
    @staticmethod
    def format_fruit(fruit):
        return {
            "id": fruit.id,
            "name": fruit.name,
            "price": fruit.price,
            "admission_date": fruit.admission_date.strftime("%d/%m/%Y"),
            "quantity": fruit.quantity,
        }

    @staticmethod
    def create_fruit(db, name, price, quantity):
        new_fruit = Fruit(name=name, price=price, quantity=quantity)
        db.add(new_fruit)
        db.commit()
        db.refresh(new_fruit)
        return FruitRepository.format_fruit(new_fruit)

    @staticmethod
    def get_fruit_by_id(db, fruit_id):
        fruit = db.get(Fruit, fruit_id)
        if not fruit:
            return None
        return FruitRepository.format_fruit(fruit)

    @staticmethod
    def get_fruit_by_name(db, name):
        stmt = select(Fruit).where(Fruit.name == name)
        fruit = db.scalar(stmt)
        if not fruit:
            return None
        return FruitRepository.format_fruit(fruit)

    @staticmethod
    def get_fruits(db):
        stmt = select(Fruit)
        return list(map(FruitRepository.format_fruit, db.scalars(stmt).all()))

    @staticmethod
    def update_fruit(db, fruit_id, name, price, quantity):
        fruit = db.get(Fruit, fruit_id)
        if fruit:
            if name is not None:
                fruit.name = name
            if price is not None:
                fruit.price = price
            if quantity is not None:
                fruit.quantity = quantity
            db.commit()
            db.refresh(fruit)
        return FruitRepository.format_fruit(fruit)

    @staticmethod
    def subtract_from_inventory(db, fruit_id, quantity):
        fruit = db.get(Fruit, fruit_id)
        if fruit:
            if quantity is not None:
                fruit.quantity = fruit.quantity - quantity
            db.commit()
            db.refresh(fruit)
        return FruitRepository.format_fruit(fruit)

    @staticmethod
    def delete_fruit(db, fruit_id):
        fruit = db.get(Fruit, fruit_id)
        if fruit:
            db.delete(fruit)
            db.commit()
            return True
        return False
