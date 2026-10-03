import pytest
from cashregister import CashRegister
from retailitem import RetailItem


def test_cashregister_accumulates():
    reg = CashRegister()
    reg.purchase_item(RetailItem("Пиджак", 12, 59.95))
    reg.purchase_item(RetailItem("Рубашка", 20, 24.95))
    assert reg.get_total() == pytest.approx(84.90)
