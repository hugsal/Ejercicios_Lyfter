from entities.addressEntity import Address
from sqlalchemy import select

class AddressRepository:
    @staticmethod
    def format_address(address):
        return {
            "id": address.id,
            "street": address.street,
            "city": address.city,
            "state": address.state,
            "zipCode": address.zip_code,
            "userId": address.fk_user_id
        }
    
    @staticmethod
    def get_addresses(db):
        return list(map(AddressRepository.format_address, db.scalars(select(Address)).all()))

    @staticmethod
    def create_address(db, street, city, state, zip_code, user_id):
        new_address = Address(street=street, city=city, state=state, zip_code=zip_code, fk_user_id=user_id)
        db.add(new_address)
        db.commit()
        db.refresh(new_address)
        return AddressRepository.format_address(new_address)
    
    @staticmethod
    def get_address_by_id(db, address_id):
        address = db.get(Address, address_id)
        if not address:
            return None
        return AddressRepository.format_address(address)

    @staticmethod
    def update_address(db, address_id, street, city, state, zip_code, user_id):
        address = db.get(Address, address_id)
        if address:
            if street is not None:
                address.street = street
            if city is not None:
                address.city = city
            if state is not None:
                address.state = state
            if zip_code is not None:
                address.zip_code = zip_code
            if user_id is not None:
                address.fk_user_id = user_id
            db.commit()
            db.refresh(address)
        return AddressRepository.format_address(address)

    @staticmethod
    def delete_address(db, address_id):
        address = db.get(Address, address_id)
        if address:
            db.delete(address)
            db.commit()
            return True
        return False