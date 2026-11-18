from bank_account import BankAccount
import pytest

@pytest.fixture
def sample():
    account = BankAccount()
    return account

def test_withraw(sample):
    sample.deposit(50000)
    assert sample.balance == 50000

def test_deposit(sample):
    sample.deposit(50000)
    assert sample.withdraw(10000) == f"successful, your balance is {sample.balance}"
    with pytest.raises(ValueError):
        sample.withdraw(50000)
