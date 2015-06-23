__author__ = 'snalam200'


def customer_purchase(self):
    print("Enter the items customer picked:")
    items_purchased = raw_input()
    return items_purchased.split(',')

