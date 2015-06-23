from GroceryStore.src.people.person import Employee

__author__ = 'snalam200'


class Manager(Employee):
    def __init__(self, name, employee_num, designation, hourly_pay, address=None, phone_num=None):
        super(Manager, self).__init__(name, employee_num, designation, hourly_pay, address, phone_num)

    def check_aisle_stock(self, aisles_dict):
        for i in aisles_dict.keys():
            if aisles_dict[i] < range(1, 4):
                print " %s supply in aisles is %s: Low" % (i, aisles_dict[i])
                # request_stock_to_aisles function
            elif aisles_dict[i] < range(4, 8):
                print "%s supply in aisles is %s: Moderate" % (i, aisles_dict[i])
            else:
                print "%s supply is in aisles %s: High" % (i, aisles_dict[i])

    def check_store_stock(self, stock_room_dict):
        for i in stock_room_dict.keys():
            if stock_room_dict[i] < range(1, 7):
                print " %s supply in store room is %s: Low" % (i, stock_room_dict[i])
                # order stock from warehouse (Later functionality)
            elif stock_room_dict[i] < range(7, 15):
                print "%s supply in store room is %s: Moderate" % (i, stock_room_dict[i])
            else:
                print "%s supply in store room is %s: High" % (i, stock_room_dict[i])

    def calculate_profit(self):
        pass
    '''Can be calculated from total price of Cashier file. How to get that here?'''

    def request_stock_to_aisles(self, aisles_dict, stock_room_dict, item):
            if stock_room_dict[item] >= (10 - aisles_dict[item]):
                stock_room_dict[item] -= (10 - aisles_dict[item])
                aisles_dict[item] = 10

    def happy_butt_check(self):
        pass