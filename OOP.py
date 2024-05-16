class Shop:
    def __init__(self, shop_name, store_type):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0

    def describe_shop(self):
        print(f"Shop name: {self.shop_name}")
        print(f"Store type: {self.store_type}")

    def open_shop(self):
        print(f"The {self.shop_name} is now open.")

    def set_number_of_units(self, units):
        self.number_of_units = units

    def increment_number_of_units(self, increment):
        self.number_of_units += increment


class Discount(Shop):
    def __init__(self, shop_name, store_type, discount_products):
        super().__init__(shop_name, store_type)
        self.discount_products = discount_products

    def get_discount_products(self):
        print("Discounted products:")
        for product in self.discount_products:
            print(product)


class User:
    def __init__(self, first_name, last_name, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
        self.additional_info = kwargs

    def describe_user(self):
        print(f"Full Name: {self.first_name} {self.last_name}")
        for key, value in self.additional_info.items():
            print(f"{key}: {value}")

    def greeting_user(self):
        print(f"Hello, {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


# admin.py

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    def __init__(self, first_name, last_name, **kwargs):
        super().__init__(first_name, last_name, **kwargs)
        self.privileges = Privileges(["Allowed to add message", "Allowed to delete users", "Allowed to ban users"])

    def show_privileges(self):
        self.privileges.show_privileges()
