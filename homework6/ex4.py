class Employee:
    def __init__(self, time_since_employment, salary):
        self.time_since_employment = time_since_employment
        self.salary = salary

    def employment_time(self):
        return self.time_since_employment


class Manager(Employee):
    def __init__(self, time_since_employment, salary, giving_employees_tasks):
        Employee.__init__(self, time_since_employment, salary)
        self.giving_employees_tasks = giving_employees_tasks

    def giving_tasks(self):
        if self.giving_employees_tasks != 0:
            return "gave tasks to his team"
        else:
            return "did not gave tasks to his team"

    def __str__(self):
        return "The manager of " + str(self.employment_time()) + " has a salary of " + str(
            self.salary) + ". And he " + str(self.giving_tasks())


class Engineer(Employee):
    def __init__(self, time_since_employment, salary, doing_projects, fixing_things):
        Employee.__init__(self, time_since_employment, salary)
        self.doing_projects = doing_projects
        self.fixing_things = fixing_things

    def is_doing_projects(self):
        if self.doing_projects != 0:
            return ". He is doing a project"
        else:
            return ". He is not doing a project"

    def is_fixing_things(self):
        if self.fixing_things != 0:
            return ". He is fixing bugs"
        else:
            return ". He is not fixing stuff"

    def __str__(self):
        return "The engineer of " + str(self.employment_time()) + " has a salary of " + str(
            self.salary) + str(self.is_doing_projects()) + str(self.is_fixing_things())


class Salesperson(Employee):
    def __init__(self, time_since_employment, salary, selling_products, making_deals):
        Employee.__init__(self, time_since_employment, salary)
        self.selling_products = selling_products
        self.making_deals = making_deals

    def is_selling_producs(self):
        if self.selling_products != 0:
            return ". He is selling a product"
        else:
            return ". He is not selling a product"

    def is_making_deals(self):
        if self.making_deals != 0:
            return ". He is making deals"
        else:
            return ". He is not making deals"

    def __str__(self):
        return "The salesperson of " + str(self.employment_time()) + " has a salary of " + str(
            self.salary) + str(self.is_selling_producs()) + str(self.is_making_deals())


manager = Manager("2 years", 3000, 0)
print(manager)

engineer = Engineer("4 years", 2000, 0, 1)
print(engineer)

salesperson = Salesperson("1 year", 1000, 0, 1)
print(salesperson)
