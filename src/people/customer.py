from GroceryStore.src.people.person import Person

__author__ = 'snalam200'


class Customer(Person):
    def __init__(self, name, address=None, phone_num=None):
        super(Customer, self).__init__(name, address, phone_num)