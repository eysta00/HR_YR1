class Employee:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def weekly_pay(self, hours):
        return 
        
class HourlyEmployee(Employee):

    def __init__(self, name, wage):
        Employee.__init__(self, name)
        self.wage = wage
    
    def weekly_pay(self, hours):
        extra_pay = 0
        weekly_pay = 0

        min_working_hours = 40
        hourly_rate_excess = 1.5

        if hours > min_working_hours:
            extra_hours = hours - min_working_hours
            excess_pay = self.wage * hourly_rate_excess
            extra_pay = extra_hours * excess_pay
            weekly_pay = min_working_hours * self.wage
            weekly_pay += extra_pay

        else:
            weekly_pay = hours * self.wage
        
        return weekly_pay

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        Employee.__init__(self, name)
        self.salary = salary
        self.bonus = bonus
    
    def weekly_pay(self, hours):
        return (self.salary / 52) + self.bonus
    
class SalariedEmployee(Employee):
    def __init__(self, name, salary):
        Employee.__init__(self, name)
        self.salary = salary

    def weekly_pay(self, hours):
        return self.salary / 52