from entities.contactsEntity import Contact


class ContactRepository:
    def format_contact(contact):
        return {
            "id": contact.id,
            "name": contact.name,
            "phone": contact.phone,
            "email": contact.email,
        }

    @staticmethod
    def create_contact(self, db, name, phone, email, user_id):
        new_contact = Contact(name=name, phone=phone, email=email, fk_user_id=user_id)
        db.add(new_contact)
        db.commit()
        db.refresh(new_contact)
        return ContactRepository.format_contact(new_contact)

    @staticmethod
    def get_contacts_by_id(self, db, contact_id):
        contact = db.get(Contact, contact_id)
        if not contact:
            return None
        return ContactRepository.format_contact(contact)

    @staticmethod
    def get_contacts_by_user_id(self, db, user_id):
        stmt = select(Contact).where(Contact.fk_user_id == user_id)
        return list(map(ContactRepository.format_contact, db.scalars(stmt).all()))

    @staticmethod
    def delete_contact(self, db, contact_id):
        contact = db.get(Contact, contact_id)
        if contact:
            db.delete(contact)
            db.commit()
            return True
        return False
