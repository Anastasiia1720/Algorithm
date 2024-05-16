# main.py

from OOP import Shop, Discount
from OOP import User
from OOP import Admin

store = Shop("MyShop", "Online")
print("Attributes:")
print("Shop Name:", store.shop_name)
print("Store Type:", store.store_type)
store.describe_shop()
store.open_shop()

print("\nNumber of Units Before:", store.number_of_units)
store.set_number_of_units(10)
print("Number of Units After:", store.number_of_units)
store.increment_number_of_units(5)
print("Number of Units After Increment:", store.number_of_units)

store_discount = Discount("DiscountShop", "Online", ["Product1", "Product2", "Product3"])
store_discount.get_discount_products()

user1 = User("John", "Doe", age=30, email="john.doe@example.com")
user1.describe_user()
user1.greeting_user()

user1.increment_login_attempts()
user1.increment_login_attempts()
print("\nLogin Attempts:", user1.login_attempts)
user1.reset_login_attempts()
print("Login Attempts After Reset:", user1.login_attempts)

admin = Admin("Admin", "User", age=40, email="admin@example.com")
admin.describe_user()
admin.show_privileges()
