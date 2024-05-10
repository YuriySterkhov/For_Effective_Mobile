class Calculation:
    def __init__(self, incomes=0, expenses=0, balance=0):
        self.incomes = incomes
        self.expenses = expenses
        self.balance = balance

    @classmethod
    def create_object(cls, notes):
        incomes = 0
        expenses = 0
        for string in sorted(notes):
            if 'Доход' in string:
                incomes += int(string[string.find('Сумма: ') + 7: string.find('\nОписание')])
            if 'Расход' in string:
                expenses += int(string[string.find('Сумма: ') + 7:string.find('\nОписание')])
        balance = incomes - expenses
        calculation_as_object = cls(incomes, expenses, balance)
        return calculation_as_object

    def object_to_string(self):
        if self.balance < 0:
            return (f'Доходы меньше расходов\nБаланс: {self.balance}\n'
                    f'Доходы: {self.incomes}\nРасходы: {self.expenses}\n')
        if self.balance > 0:
            return (f'Доходы больше расходов\nБаланс: {self.balance}\n'
                    f'Доходы: {self.incomes}\nРасходы: {self.expenses}\n')
        else:
            if self.incomes == self.expenses == 0:
                return (f'Доходы равны расходам\nБаланс: {self.balance}\n'
                        f'Доходы: {self.incomes}\n'
                        f'Расходы: {self.expenses}\n'
                        f'Проверьте содержимое файла data_file.txt, возможно, он пуст\n')
            else:
                return (f'Доходы равны расходам\nБаланс: {self.balance}\n'
                        f'Доходы: {self.incomes}\nРасходы: {self.expenses}\n')
