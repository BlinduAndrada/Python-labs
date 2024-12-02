class Account:
    def __init__(self, initial_sum, sum_to_add, sum_to_get):
        self.sum_to_add = sum_to_add
        self.sum_to_get = sum_to_get
        self.initial_sum = initial_sum

    def deposit(self):
        total_sum = self.initial_sum + self.sum_to_add
        return "You deposit the sum " + str(self.sum_to_add) + ". Now your new total is " + str(total_sum)


    def withdrawal(self):
        if self.sum_to_get > self.initial_sum:
            return "You dont have enough money"
        new_sum = self.initial_sum - self.sum_to_get
        return "You got the sum " + str(self.sum_to_get) + ". Now your new total is " + str(new_sum)


class CheckingAccount(Account):
    def __init__(self,initial_sum,sum_to_add,sum_to_get):
        Account.__init__(self, initial_sum, sum_to_add, sum_to_get)


class SavingsAccount(Account):
    def __init__(self, initial_sum, sum_to_add, sum_to_get,goal):
        Account.__init__(self, initial_sum, sum_to_add, sum_to_get)
        self.goal=goal

    def interest_calculation(self):
        if self.goal<=self.initial_sum:
            return "Congrats , you achieved your goal!"
        else:
            return "You still didn't achieved your goal. You still need to save up the sum " + str(self.goal-self.initial_sum)

check= CheckingAccount(1000,50,1100)
print(check.deposit())
print(check.withdrawal())


save= SavingsAccount(1000,0,0,1500)
print(save.interest_calculation())