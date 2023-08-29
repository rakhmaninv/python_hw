# Напишите программу банкомат.
#  Начальная сумма равна нулю
#  Допустимые действия: пополнить, снять, выйти
#  Сумма пополнения и снятия кратны 50 у.е.
#  Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
#  После каждой третей операции пополнения или снятия начисляются проценты - 3%
#  Нельзя снять больше, чем на счёте
#  При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
#  Любое действие выводит сумму денег
#  Дополнительно сохраняйте все операции поступления и снятия средств в список.

class Atm:
    __balance = 0
    __operation_count = 0
    fee_max = 600
    fee_min = 30
    wealth_tax_rate = 0.1
    taxable_min = 5_000_000
    interest = 0.03
    fee_rate = 0.015

    def deposit(self, amount: int | float):
        self._charge_tax()
        self._balance += amount
        self._operation_count_check()

    def withdraw(self, amount: int | float):
        self._charge_tax()
        amount += self._calculate_fee(amount)
        if self._balance >= amount:
            self._balance -= amount
            self._operation_count_check()
        else:
            raise ValueError(f'Сумма с комиссией({amount}) больше баланса.')

    def show_balance(self):
        return self._balance

    def _operation_count_check(self):
        self._operation_count += 1
        if self._operation_count == 3:
            self._deposit_interest()
            self._operation_count = 0

    def _deposit_interest(self):
        interest = self._balance * self.interest
        self._balance += interest

    def _calculate_fee(self, amount):
        fee = amount * self.fee_rate
        return self.fee_min if fee <= self.fee_min else self.fee_max if fee >= self.fee_max else fee

    def _charge_tax(self):
        if self._balance > self.taxable_min:
            self._balance -= self._balance * self.wealth_tax_rate




if __name__ == '__main__':

    a = 2
    a -= 1 + 1
    print(a)

