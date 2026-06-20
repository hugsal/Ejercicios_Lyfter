from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def has_permission(self, permission):
        pass


class AdminUser(User):
    permissions = ("read", "write", "delete")

    def get_role(self):
        print("Admin")
        return

    def has_permission(self, permission):
        return permission in self.permissions


class RegularUser(User):
    permissions = ("read",)

    def get_role(self):
        print("Regular")
        return

    def has_permission(self, permission):
        return permission in self.permissions


user1 = AdminUser("Juan")
user2 = RegularUser("Hugo")

user1.get_role()
print(user1.has_permission("write"))
print(user1.has_permission("delete"))

user2.get_role()
print(user2.has_permission("write"))
print(user2.has_permission("read"))
