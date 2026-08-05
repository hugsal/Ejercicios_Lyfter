from entities.userEntity import User
from sqlalchemy import select


class UserRepository:
    @staticmethod
    def format_user(user):
        return {"id": user.id, "name": user.name, "email": user.email, "userName": user.user_name}

    @staticmethod
    def create_user(db, name, email, user_name):
        new_user = User(name=name, email=email, user_name=user_name)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return UserRepository.format_user(new_user)

    @staticmethod
    def get_user_by_id(db, user_id):
        user = db.get(User, user_id)
        if not user:
            return None
        return UserRepository.format_user(user)

    @staticmethod
    def get_user_by_name(db, user_name):
        stmt = select(User).where(User.user_name == user_name)
        user = db.scalar(stmt)
        if not user:
            return None
        return UserRepository.format_user(user)

    @staticmethod
    def get_user_by_email(db, email):
        stmt = select(User).where(User.email == email)
        user = db.scalar(stmt)
        if not user:
            return None
        return UserRepository.format_user(user)

    @staticmethod
    def get_users(db):
        stmt = select(User)
        return list(map(UserRepository.format_user, db.scalars(stmt).all()))

    @staticmethod
    def update_user(db, user_id, name, email, usr):
        user = db.get(User, user_id)
        if user:
            if name is not None:
                user.name = name
            if usr is not None:
                user.user_name = usr
            if email is not None:
                user.email = email
            db.commit()
            db.refresh(user)
        return UserRepository.format_user(user)

    @staticmethod
    def delete_user(db, user_id):
        user = db.get(User, user_id)
        if user:
            db.delete(user)
            db.commit()
            return True
        return False