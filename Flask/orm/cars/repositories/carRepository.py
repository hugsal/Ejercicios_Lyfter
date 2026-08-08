from entities.carEntity import Car
from sqlalchemy import select

class CarRepository:
    @staticmethod
    def format_car(car):
        return {
            "id": car.id,
            "brand": car.brand,
            "model": car.model,
            "year": car.year,
            "userId": car.fk_user_id
        }
    
    @staticmethod
    def get_cars(db):
        return list(map(CarRepository.format_car, db.scalars(select(Car)).all()))

    @staticmethod
    def create_car(db, brand, model, year, fk_user_id):
        new_car = Car(brand=brand, model=model, year=year, fk_user_id=fk_user_id)
        db.add(new_car)
        db.commit()
        db.refresh(new_car)
        return CarRepository.format_car(new_car)
    
    @staticmethod
    def get_car_by_id(db, car_id):
        car = db.get(Car, car_id)
        if not car:
            return None
        return CarRepository.format_car(car)

    @staticmethod
    def update_car(db, car_id, brand, model, year, user_id):
        car = db.get(Car, car_id)
        if car:
            if brand is not None:
                car.brand = brand
            if model is not None:
                car.model = model
            if year is not None:
                car.year = year
            if user_id is not None:
                car.fk_user_id = user_id
            db.commit()
            db.refresh(car)
        return CarRepository.format_car(car)

    @staticmethod
    def delete_car(db, car_id):
        car = db.get(Car, car_id)
        if car:
            db.delete(car)
            db.commit()
            return True
        return False