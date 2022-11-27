def tax_calc(money: int, rate: float = 0.35) -> int:
    return int(money * rate)


def pay_tax(tax: int) -> None:
    print("thank you for paying", tax)


pay_tax(tax_calc(150000000))
