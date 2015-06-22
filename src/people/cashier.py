from GroceryStore.src.people.person import Employee

__author__ = 'snalam200'


class Cashier(Employee):
    def __init__(self, name, employee_num, designation, hourly_pay, address=None, phone_num=None):
        super(Cashier, self).__init__(name, employee_num, designation, hourly_pay, address, phone_num)

    @staticmethod
    def customer_purchase():
        print("Enter the items customer picked:")
        items_purchased = raw_input()
        return items_purchased.split(',')

    @staticmethod
    def get_prices(purchase_list, price_stock_dict):
        for item in purchase_list:
            total_price = 0
            item_price = price_stock_dict[item][0]
            total_price += item_price
            return total_price

    @staticmethod
    def update_stock(purchase_list, price_stock_dict):
        for item in purchase_list:
            price_stock_dict[item][1] -= 1
        return price_stock_dict