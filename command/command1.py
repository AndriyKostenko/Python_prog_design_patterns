from abc import ABC, abstractmethod
from enum import Enum
import unittest


class BankAccount:
    # Maximum allowed overdraft
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        """Deposit money into the account."""
        self.balance += amount
        print(f"Deposited {amount}, Balance = {self.balance}")

    def withdraw(self, amount):
        """
        Attempt to withdraw money.
        Returns True if successful, False if overdraft limit would be exceeded.
        """
        if (self.balance - amount) >= BankAccount.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f"Withdrew {amount}, Balance = {self.balance}")
            return True
        return False

    def __str__(self):
        return f"Balance = {self.balance}"


class Command(ABC):
    """Abstract base class for all commands."""

    def __init__(self):
        self.success = False

    @abstractmethod
    def invoke(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class Action(Enum):
    DEPOSIT = 0
    WITHDRAW = 1


class BankAccountCommand(Command):
    """Single command for deposit or withdrawal"""

    def __init__(self, account, action, amount):
        super().__init__()
        self.account = account
        self.amount = amount
        self.action = action

    def invoke(self):
        if self.action == Action.DEPOSIT:
            self.account.deposit(self.amount)
            self.success = True
        elif self.action == Action.WITHDRAW:
            self.success = self.account.withdraw(self.amount)

    def undo(self):
        if not self.success:
            return

        if self.action == Action.DEPOSIT:
            self.account.withdraw(self.amount)
        elif self.action == Action.WITHDRAW:
            self.account.deposit(self.amount)


class CompositeBankAccountCommand(Command):
    """Composite command holding multiple commands"""

    def __init__(self, commands=None):
        super().__init__()
        self.commands = list(commands) if commands else []

    def invoke(self):
        for c in self.commands:
            c.invoke()
        self.success = all(cmd.success for cmd in self.commands)

    def undo(self):
        for c in reversed(self.commands):
            c.undo()


class MoneyTransferCommans(CompositeBankAccountCommand):
    """Transfer money between accounts using a composite command"""

    def __init__(self, from_acc, to_acc, amount):
        withdraw_cmd = BankAccountCommand(from_acc, Action.WITHDRAW, amount)
        deposit_cmd = BankAccountCommand(to_acc, Action.DEPOSIT, amount)

        super().__init__([withdraw_cmd, deposit_cmd])

    def invoke(self):
        flag = True
        for cmd in self.commands:
            if flag:
                cmd.invoke()
                flag = cmd.success
            else:
                cmd.success = False

        self.success = flag  # Only true if both succeeded


class TestSuite(unittest.TestCase):

    def test_better_transfer(self):
        ba1 = BankAccount(100)
        ba2 = BankAccount()

        amount = 1000
        transfer = MoneyTransferCommans(ba1, ba2, amount)
        transfer.invoke()

        print(f"ba1: {ba1}, ba2: {ba2}")
        transfer.undo()
        print(f"ba1: {ba1}, ba2: {ba2}")
        print("Transfer success:", transfer.success)


if __name__ == '__main__':
    unittest.main()
