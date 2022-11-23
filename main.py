from flat import Bill, Flatmate
from reports import PdfReport


amount = float(input("Hey user, enter the bill amount "))
period = input("Whats is the bill period? E.g. December 2020: ")

name1 = input("Whats is your name? ")
days1 = int(input(f"How many did {name1} stay in the house during the bill period "))

name2 = input("Whats is your name? ")
days2 = int(input(f"How many did {name2} stay in the house during the bill period "))

the_bill = Bill(amount, period)
flatmate1 = Flatmate(name=name1, days_in_house=days1)
flatmate2 = Flatmate(name=name2, days_in_house=days2)

print(f"{flatmate1.name} pays: {flatmate1.pays(the_bill, flatmate2)}")
print(f"{flatmate2.name} pays: {flatmate2.pays(the_bill, flatmate1)}")

pdf_report = PdfReport(filename=f"Report_{the_bill.period}.pdf")
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill_to_pay=the_bill)