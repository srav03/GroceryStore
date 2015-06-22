__author__ = 'snalam200'


class Person(object):
    def __init__(self, name, address=None, phone_num=None):
        self.name = name
        self.address = address
        self.phone_num = phone_num


class Employee(Person):
    def __init__(self, name, employee_num, designation, hourly_pay, address=None, phone_num=None):
        super(Employee, self).__init__(name, address, phone_num)
        self.employee_num = employee_num
        self.designation = designation
        self.hourly_pay = float(hourly_pay)



