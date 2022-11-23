class Bill:
    def __init__(self, amount: int, period: str):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Create a flatmate person who live in the flat
    and pays a share of a bill
    """
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill_to_pay, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill_to_pay.amount * weight
        return to_pay
