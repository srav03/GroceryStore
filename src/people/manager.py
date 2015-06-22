from GroceryStore.src.people.person import Employee

__author__ = 'snalam200'


class Manager(Employee):
    def __init__(self, name, employee_num, designation, hourly_pay, address=None, phone_num=None):
        super(Manager, self).__init__(name, employee_num, designation, hourly_pay, address, phone_num)

    def check_aisle_stock(self):
        pass

    def check_store_stock(self):
        pass

    def calculate_profit(self):
        pass

    def request_stock_to_aisles(self):
        pass

    def happy_butt_check(self):
        pass