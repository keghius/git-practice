import pytest

from orderlab.pricing import final_total, subtotal


# == Level 1 : Basic Test Cases ==
def test_subtotal_normal():
    assert subtotal(10_000, 2) == 20_000


def test_subtotal_zero():
    assert subtotal(0, 3) == 0


def test_subtotal_negative():
    with pytest.raises(ValueError):
        subtotal(-100, 2)


# == Level 2 : Advanced Test Cases ==
def test_discount_below_zero():
    with pytest.raises(ValueError):
        final_total(10_000, 2, -1)


def test_discount_over_100():
    with pytest.raises(ValueError, match="invalid discount"):
        final_total(10_000, 2, 101)


@pytest.mark.parametrize(
    "price, qty, discount, expected",
    [
        (10_000, 2, 0, 23_000),
        (49_999, 1, 0, 52_999),
        (50_000, 1, 0, 50_000),
        (10_000, 2, 10, 21_000),
    ],
)
def test_final_total(price, qty, discount, expected):
    assert final_total(price, qty, discount) == expected


@pytest.mark.parametrize("bad_discount", [-1, 101])
def test_invalid_discount(bad_discount):
    with pytest.raises(ValueError, match="invalid discount"):
        final_total(10_000, 2, bad_discount)


# == Level 3 : CSV Test Cases ==
